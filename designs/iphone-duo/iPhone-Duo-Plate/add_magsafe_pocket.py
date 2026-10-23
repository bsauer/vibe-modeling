#!/usr/bin/env python3
"""Add a 25 W MagSafe pocket, slot vent grille, thumb notch, and back-edge cable
raceway to the 260 mm sloped iPhone Duo plate, and build production-derived
fit coupons from the same geometry.

Governing plan: plans/current/2026-10-22-14-32-52_iphone-duo-plate-magsafe-pocket.md
Design detail:  .cursor/plans/plate_magsafe_pocket_b889b55d.plan.md

Coordinates are the source mesh's local frame: origin at the plate center,
X along the 260 mm length (+X = camera half), Y along 173 mm (+Y = back edge,
camera end of the phone), Z from -6 (bottom) to +6 (rim top).

Run with the pinned project environment:

    uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --coupons
    uv run python designs/iphone-duo/iPhone-Duo-Plate/add_magsafe_pocket.py --plate
"""

from __future__ import annotations

import argparse
import math
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path

import manifold3d as m3
import numpy as np

Manifold = m3.Manifold
CS = m3.CrossSection
ROUND = m3.JoinType.Round

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE_3MF = HERE / "iPhone Duo Plate 260 sloped.3mf"
OUTPUT_DIR = REPO / "output" / "iphone-duo"
COUPON_3MF = OUTPUT_DIR / "iPhone Duo Plate MagSafe fit coupons.3mf"
PLATE_3MF = OUTPUT_DIR / "iPhone Duo Plate 260 sloped magsafe.3mf"

# --- Governance -------------------------------------------------------------
minimum_wall_thickness = 2.0
minimum_structural_overlap = 2.0  # declared; one solid, no printed joins
assert minimum_structural_overlap >= minimum_wall_thickness

# --- Source plate (measured from the mesh) ----------------------------------
plate_bottom_z = -6.0
plate_top_z = 6.0
floor_top_z = 0.75  # well floor, 6.75 mm above the bottom
well_x = (-82.5, 83.3)
well_y = (-59.1, 59.9)
well_corner_r = 16.9
camera_slot_x = (15.5, 82.5)  # stadium, full round ends
camera_slot_y = (29.1, 59.1)
old_vent_count = 20
old_vent_d = 18.0
old_vent_fill_d = 18.4  # plug overlaps the hole wall by 0.2 mm radially
source_bed_offset = (135.5, 136.0, 6.0)  # source 3MF build transform

# --- Puck and pocket --------------------------------------------------------
puck_center = (41.2, -2.3)  # X-ray ring-center estimate; template confirms
bore_d = 56.0  # tuned by coupons: 55.8 / 56.0 / 56.2
bore_depth = 4.6  # from the well floor
ledge_opening_d = 34.0
bore_segments = 256
ledge_bottom_z = floor_top_z - bore_depth
ledge_thickness = ledge_bottom_z - plate_bottom_z

# --- Cable path -------------------------------------------------------------
gate_w = 5.0
gate_radial_inset = 3.0  # gate starts this far inside the bore radius
floor_slot_w = 3.0
raceway_w = 2.8
raceway_depth = 3.4  # 0.8 mm pinch lip + 2.6 mm clear for the 2.35 mm braid
raceway_start_x = 80.0  # overlaps the floor slot for a continuous path
raceway_turn_x = well_x[1]  # turn begins under the solid rim
raceway_bend_r = 20.0
pinch_w = 2.05  # tuned by coupons: 1.90 / 2.05 / 2.20
pinch_h = 0.8
pinch_len = 3.0
pinch_s = (6.0, 22.0, 75.0)  # path distance from raceway_start_x

# --- Vent grille ------------------------------------------------------------
vent_slot_width = 4.0
vent_slot_pitch = 7.5
vent_border_margin = 7.0
vent_feature_margin = 6.0
vent_spine_width = 10.0
vent_min_slot_length = 15.0
vent_top_chamfer = 0.5
hinge_x = (well_x[0] + well_x[1]) / 2

# --- Thumb notch ------------------------------------------------------------
notch_w = 25.0
notch_into_rim = 12.0
notch_into_floor = 3.5
notch_dip = 1.5  # below the well floor at the well edge
notch_corner_r = 4.0

# --- Coupons ----------------------------------------------------------------
coupon_crop_x = (10.4, 112.0)  # 1 mm clear of the x=7.4 grille slot and its chamfer
coupon_crop_y = (-40.0, 28.0)
coupon_variants = ((55.8, 1.90), (56.0, 2.05), (56.2, 2.20))
label_notch_w = 2.0
label_notch_depth = 2.0
label_notch_pitch = 5.0
label_notch_x0 = 95.0
template_hole_d = 66.0
# The hole would cut into the camera opening, so its +Y side is a flat edge
# that keeps the 2.0 mm minimum strip. Gaps read with calipers give the offset:
#   dx = (gap_+X - gap_-X) / 2
#   dy = (gap_-Y - gap_+Y - template_dy_nominal) / 2
template_hole_flat_y = camera_slot_y[0] - minimum_wall_thickness
template_dy_nominal = (template_hole_d / 2) - (template_hole_flat_y - puck_center[1])
template_sheet = 0.8
template_wall = 2.4
template_lip = 3.0

# --- Bed ----------------------------------------------------------------------
bed_size = 270.0
bed_margin = 5.0
bed_gap = 8.0

EPS = 0.01

assert ledge_thickness >= minimum_wall_thickness, ledge_thickness
assert (bore_d - ledge_opening_d) / 2 >= minimum_wall_thickness
assert vent_slot_pitch - vent_slot_width - 2 * vent_top_chamfer >= minimum_wall_thickness
assert raceway_depth - pinch_h > 2.35
assert raceway_w > pinch_w
for d, p in coupon_variants:
    assert d > 55.5 and p < 2.35


# --- Helpers ----------------------------------------------------------------
def circle(c, d, seg=bore_segments) -> CS:
    return CS.circle(d / 2, seg).translate(c)


def rrect(x0, x1, y0, y1, r=0.0) -> CS:
    if r <= 0:
        return CS.square([x1 - x0, y1 - y0]).translate([x0, y0])
    return CS.batch_hull([
        circle((x0 + r, y0 + r), 2 * r, 96), circle((x1 - r, y0 + r), 2 * r, 96),
        circle((x0 + r, y1 - r), 2 * r, 96), circle((x1 - r, y1 - r), 2 * r, 96),
    ])


def pill_y(x, y0, y1, w) -> CS:
    return CS.batch_hull([circle((x, y0 + w / 2), w, 64), circle((x, y1 - w / 2), w, 64)])


def prism(cs: CS, z0: float, z1: float) -> Manifold:
    return cs.extrude(z1 - z0).translate([0, 0, z0])


def load_3mf(path: Path) -> Manifold:
    verts, tris, off = [], [], 0
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.endswith(".model"):
                continue
            s = z.read(name).decode()
            v = re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', s)
            t = re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', s)
            if v:
                verts.append(np.array(v, float))
                tris.append(np.array(t, np.int64) + off)
                off += len(v)
    mesh = m3.Mesh(vert_properties=np.vstack(verts).astype(np.float32),
                   tri_verts=np.vstack(tris).astype(np.uint32))
    m = Manifold(mesh)
    assert m.status() == m3.Error.NoError, m.status()
    return m


def write_3mf(path: Path, objects: list[tuple[str, Manifold, tuple[float, float, float]]]) -> None:
    """Model-only 3MF: one mesh object per part, placed by build-item transforms."""
    parts = []
    items = []
    for i, (name, m, (tx, ty, tz)) in enumerate(objects, start=1):
        mesh = m.to_mesh()
        v = np.asarray(mesh.vert_properties)[:, :3]
        t = np.asarray(mesh.tri_verts)
        vs = "".join(f'<vertex x="{a:.5f}" y="{b:.5f}" z="{c:.5f}"/>' for a, b, c in v)
        ts = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in t)
        parts.append(f'<object id="{i}" type="model" name="{name}"><mesh><vertices>{vs}</vertices>'
                     f'<triangles>{ts}</triangles></mesh></object>')
        items.append(f'<item objectid="{i}" transform="1 0 0 0 1 0 0 0 1 {tx:.4f} {ty:.4f} {tz:.4f}" printable="1"/>')
    model = ('<?xml version="1.0" encoding="UTF-8"?>\n'
             '<model unit="millimeter" xml:lang="en-US" '
             'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
             '<metadata name="Application">vibe-modeling add_magsafe_pocket.py</metadata>'
             f'<resources>{"".join(parts)}</resources><build>{"".join(items)}</build></model>')
    ctypes = ('<?xml version="1.0" encoding="UTF-8"?>\n'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>'
              '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Target="/3D/3dmodel.model" Id="rel0" '
            'Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in (("[Content_Types].xml", ctypes), ("_rels/.rels", rels), ("3D/3dmodel.model", model)):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))  # reproducible bytes
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    tmp.replace(path)


# --- Features ------------------------------------------------------------------
def well_cs() -> CS:
    return rrect(well_x[0], well_x[1], well_y[0], well_y[1], well_corner_r)


def camera_slot_cs() -> CS:
    return rrect(camera_slot_x[0], camera_slot_x[1], camera_slot_y[0], camera_slot_y[1],
                 (camera_slot_y[1] - camera_slot_y[0]) / 2)


def old_vent_centers(plate: Manifold) -> list[tuple[float, float]]:
    cs = plate.slice(plate_bottom_z + 0.5)
    centers = []
    target = math.pi * (old_vent_d / 2) ** 2
    for poly in cs.to_polygons():
        p = np.asarray(poly)
        x, y = p[:, 0], p[:, 1]
        area = abs((x * np.roll(y, -1) - np.roll(x, -1) * y).sum() / 2)
        if abs(area - target) < 0.05 * target:
            centers.append(tuple(((p.min(0) + p.max(0)) / 2).round(3)))
    assert len(centers) == old_vent_count, centers
    return centers


def floor_slot_cs(bore: float) -> CS:
    x0 = puck_center[0] + bore / 2 - gate_radial_inset
    return rrect(x0, well_x[1], puck_center[1] - floor_slot_w / 2, puck_center[1] + floor_slot_w / 2)


def gate_cs(bore: float) -> CS:
    x0 = puck_center[0] + bore / 2 - gate_radial_inset
    return rrect(x0, x0 + gate_radial_inset + 1.0, puck_center[1] - gate_w / 2, puck_center[1] + gate_w / 2)


def notch_footprint_cs() -> CS:
    yc = (well_y[0] + well_y[1]) / 2
    return rrect(well_x[0] - notch_into_rim, well_x[0] + notch_into_floor,
                 yc - notch_w / 2, yc + notch_w / 2, notch_corner_r)


def notch_solid() -> Manifold:
    yc = (well_y[0] + well_y[1]) / 2
    low = rrect(well_x[0] - 1.0, well_x[0] + notch_into_floor, yc - notch_w / 2, yc + notch_w / 2, notch_corner_r)
    top = notch_footprint_cs()
    return Manifold.batch_hull([prism(low, floor_top_z - notch_dip, floor_top_z - notch_dip + EPS),
                                prism(top, plate_top_z + 1.0, plate_top_z + 1.0 + EPS)])


def raceway_path(y_end: float) -> np.ndarray:
    """Centerline: +X under the floor slot, 90 deg bend to +Y, straight to y_end."""
    y0 = puck_center[1]
    pts = [(raceway_start_x, y0), (raceway_turn_x, y0)]
    cx, cy = raceway_turn_x, y0 + raceway_bend_r
    for a in np.linspace(-math.pi / 2, 0, 48)[1:]:
        pts.append((cx + raceway_bend_r * math.cos(a), cy + raceway_bend_r * math.sin(a)))
    pts.append((cx + raceway_bend_r, y_end))
    return np.array(pts)


def band_cs(path: np.ndarray, half_w: float) -> CS:
    """Butt-ended band of half width half_w along a polyline."""
    d = np.gradient(path, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None]
    n = np.c_[-d[:, 1], d[:, 0]]
    poly = np.vstack([path + n * half_w, (path - n * half_w)[::-1]])
    x, y = poly[:, 0], poly[:, 1]
    if (x * np.roll(y, -1) - np.roll(x, -1) * y).sum() < 0:
        poly = poly[::-1]  # manifold treats clockwise contours as holes
    return CS([poly])


def sub_path(path: np.ndarray, s0: float, s1: float) -> np.ndarray:
    seg = np.linalg.norm(np.diff(path, axis=0), axis=1)
    s = np.r_[0, np.cumsum(seg)]
    fine = np.linspace(s0, s1, 12)
    return np.c_[np.interp(fine, s, path[:, 0]), np.interp(fine, s, path[:, 1])]


def raceway_solid(pinch: float) -> Manifold:
    path = raceway_path(100.0)
    full = band_cs(path, raceway_w / 2)
    lips = CS()
    for s in pinch_s:
        sp = sub_path(path, s, s + pinch_len)
        clear = sub_path(path, s - 0.5, s + pinch_len + 0.5)  # overrun avoids zero-width slivers at lip ends
        lips = lips + (band_cs(sp, raceway_w / 2 + 0.5) - band_cs(clear, pinch / 2))
    mouth = full - lips
    lip_top = plate_bottom_z + pinch_h
    return (prism(mouth, plate_bottom_z - 1.0, lip_top + EPS)
            + prism(full, lip_top, plate_bottom_z + raceway_depth))


def top_height(plate: Manifold, x: float, y: float) -> float:
    """Highest Z (0.05 mm resolution) whose slice contains (x, y)."""
    pt = CS.square([0.02, 0.02], center=True).translate([x, y])
    lo = plate_bottom_z
    for z in np.arange(plate_bottom_z + 0.05, plate_top_z, 0.05):
        if (plate.slice(z) ^ pt).area() > 0:
            lo = z
        else:
            break
    return lo


def exit_notch_solid(plate: Manifold) -> tuple[Manifold, float]:
    """Open the raceway through the full height where its roof would drop below
    minimum_wall_thickness near the sloped back edge."""
    x = raceway_turn_x + raceway_bend_r
    need = plate_bottom_z + raceway_depth + minimum_wall_thickness
    y = puck_center[1] + raceway_bend_r
    while y < 90 and top_height(plate, x, y) >= need:
        y += 0.25
    y_cut = y - 1.0  # start the open notch slightly before the roof thins
    cs = rrect(x - raceway_w / 2, x + raceway_w / 2, y_cut, 100.0)
    return prism(cs, plate_bottom_z - 1.0, plate_top_z + 1.0), y_cut


def grille_slots(bore: float) -> list[tuple[float, float, float]]:
    border = well_cs().offset(-vent_border_margin, ROUND, circular_segments=128)
    allowed = border
    for k in (camera_slot_cs(), circle(puck_center, bore), floor_slot_cs(bore), notch_footprint_cs()):
        allowed = allowed - k.offset(vent_feature_margin, ROUND, circular_segments=128)
    allowed = allowed - rrect(hinge_x - vent_spine_width / 2, hinge_x + vent_spine_width / 2, -90, 90)
    first = vent_spine_width / 2 + vent_slot_width / 2
    xs = sorted({round(hinge_x + sgn * (first + k * vent_slot_pitch), 4)
                 for sgn in (-1, 1) for k in range(14)})
    slots = []
    for x in xs:
        column = rrect(x - vent_slot_width / 2, x + vent_slot_width / 2, -90, 90)
        reach = border ^ column
        if reach.is_empty() or reach.area() <= 0:
            continue
        _, ry0, _, ry1 = reach.bounds()
        for poly in (allowed ^ column).decompose():
            if poly.is_empty() or poly.area() <= 0:
                continue
            bx0, by0, bx1, by1 = poly.bounds()
            if bx1 - bx0 < vent_slot_width - 0.01:
                continue  # clipped sideways by a margin curve
            if by1 - by0 < vent_min_slot_length:
                continue  # fragment too short to read as part of the grille
            if abs(by0 - ry0) > 0.05 and abs(by1 - ry1) > 0.05:
                continue  # orphan island between features, not anchored to the border
            slots.append((x, by0, by1))
    return slots


def grille_solid(slots) -> Manifold:
    w0, w1 = vent_slot_width, vent_slot_width + 2 * vent_top_chamfer
    cuts = []
    for x, y0, y1 in slots:
        straight = prism(pill_y(x, y0, y1, w0), plate_bottom_z - 1.0, floor_top_z - vent_top_chamfer + EPS)
        cham = Manifold.batch_hull([
            prism(pill_y(x, y0, y1, w0), floor_top_z - vent_top_chamfer, floor_top_z - vent_top_chamfer + EPS),
            prism(pill_y(x, y0 - vent_top_chamfer, y1 + vent_top_chamfer, w1), floor_top_z + EPS, floor_top_z + 0.5),
        ])
        cuts += [straight, cham]
    return Manifold.batch_boolean(cuts, m3.OpType.Add)


@dataclass
class Built:
    solid: Manifold
    slots: list
    exit_y: float
    vents: list


def build_plate(source: Manifold, bore: float = bore_d, pinch: float = pinch_w) -> Built:
    vents = old_vent_centers(source)
    plugs = [prism(circle(c, old_vent_fill_d, 128), plate_bottom_z, floor_top_z) for c in vents]
    solid = Manifold.batch_boolean([source] + plugs, m3.OpType.Add)
    slots = grille_slots(bore)
    exit_cut, exit_y = exit_notch_solid(solid)
    cuts = [
        grille_solid(slots),
        prism(circle(puck_center, bore), ledge_bottom_z, plate_top_z + 1.0),
        prism(circle(puck_center, ledge_opening_d), plate_bottom_z - 1.0, plate_top_z + 1.0),
        prism(gate_cs(bore), plate_bottom_z - 1.0, plate_top_z + 1.0),
        prism(floor_slot_cs(bore), plate_bottom_z - 1.0, plate_top_z + 1.0),
        raceway_solid(pinch),
        exit_cut,
        notch_solid(),
    ]
    solid = solid - Manifold.batch_boolean(cuts, m3.OpType.Add)
    return Built(solid, slots, exit_y, vents)


def label_notches(n: int) -> Manifold:
    cuts = []
    for i in range(n):
        x = label_notch_x0 + i * label_notch_pitch
        y = coupon_crop_y[0]
        tri = CS([np.array([(x - label_notch_w / 2, y - 0.5), (x + label_notch_w / 2, y - 0.5),
                            (x, y + label_notch_depth)])])
        cuts.append(prism(tri, plate_bottom_z - 1.0, plate_top_z + 1.0))
    return Manifold.batch_boolean(cuts, m3.OpType.Add)


def build_coupon(source: Manifold, idx: int) -> Manifold:
    bore, pinch = coupon_variants[idx]
    plate = build_plate(source, bore, pinch).solid
    box = prism(rrect(coupon_crop_x[0], coupon_crop_x[1], coupon_crop_y[0], coupon_crop_y[1]),
                plate_bottom_z - 1.0, plate_top_z + 1.0)
    return (plate ^ box) - label_notches(idx + 1)


def build_template() -> Manifold:
    """Thin replica of the well: sheet plus perimeter lip. Printed lip up, then
    laid over the back of the open phone so the puck can self-center in the
    oversized hole. Same frame as the plate, so no mirroring is needed."""
    outer = well_cs().offset(template_wall, ROUND, circular_segments=128)
    hole = circle(puck_center, template_hole_d) ^ rrect(-200, 200, -200, template_hole_flat_y)
    sheet = outer - camera_slot_cs() - hole
    lip = outer - well_cs()
    return prism(sheet, 0.0, template_sheet) + prism(lip, 0.0, template_sheet + template_lip)


# --- Verification ------------------------------------------------------------
def thin_regions(cs: CS, ignore: CS | None = None, tol_area: float = 0.5):
    """Material narrower than minimum_wall_thickness, by morphological opening."""
    r = minimum_wall_thickness / 2 - 0.01
    opened = cs.offset(-r, ROUND, circular_segments=64).offset(r, ROUND, circular_segments=64)
    thin = cs - opened
    if ignore is not None:
        thin = thin - ignore
    out = []
    for piece in thin.decompose():
        if piece.area() > tol_area:
            out.append((round(piece.area(), 2), tuple(round(v, 1) for v in piece.bounds())))
    return out


def report(name: str, m: Manifold) -> None:
    bb = m.bounding_box()
    comps = len(m.decompose())
    print(f"[verify] {name}: status={m.status().name} shells={comps} genus={m.genus()} "
          f"volume={m.volume():.1f} mm3 bounds=({bb[0]:.2f},{bb[1]:.2f},{bb[2]:.2f})-({bb[3]:.2f},{bb[4]:.2f},{bb[5]:.2f})")
    assert m.status() == m3.Error.NoError
    assert comps == 1, f"{name}: {comps} shells"


def fit_circle(m: Manifold, z: float, r_expect: float) -> tuple[float, float, float]:
    """Least-squares circle through contour points within 0.6 mm of r_expect
    around the puck center (the gate interrupts the bore contour)."""
    pts = np.vstack([np.asarray(p) for p in m.slice(z).to_polygons()])
    r = np.hypot(pts[:, 0] - puck_center[0], pts[:, 1] - puck_center[1])
    p = pts[np.abs(r - r_expect) < 0.6]
    assert len(p) > 64, f"too few contour points near r={r_expect} at z={z}"
    a = np.c_[2 * p[:, 0], 2 * p[:, 1], np.ones(len(p))]
    c = np.linalg.lstsq(a, (p ** 2).sum(1), rcond=None)[0]
    return c[0], c[1], 2 * math.sqrt(c[2] + c[0] ** 2 + c[1] ** 2)


def verify_coupon(name: str, m: Manifold, bore: float, pinch: float) -> None:
    report(name, m)
    cx, cy, d = fit_circle(m, floor_top_z - 1.0, bore / 2)
    print(f"[verify] {name}: bore center=({cx:.3f},{cy:.3f}) d={d:.3f}")
    assert abs(cx - puck_center[0]) < 0.1 and abs(cy - puck_center[1]) < 0.1
    assert abs(d - bore) < 0.05
    cx, cy, d = fit_circle(m, plate_bottom_z + 1.0, ledge_opening_d / 2)
    print(f"[verify] {name}: ledge opening d={d:.3f}, ledge thickness={ledge_thickness:.2f}")
    assert abs(d - ledge_opening_d) < 0.05
    # Pinch width at the mouth: cross the raceway at the first pinch midpoint.
    path = raceway_path(100.0)
    s_mid = pinch_s[0] + pinch_len / 2
    pair = sub_path(path, s_mid, s_mid + 0.01)
    mid, t = pair[0], (pair[-1] - pair[0]) / np.linalg.norm(pair[-1] - pair[0])
    n = np.array([-t[1], t[0]])
    probe = band_cs(np.array([mid - 3 * n, mid + 3 * n]), 0.05)  # perpendicular to the path
    cs = m.slice(plate_bottom_z + pinch_h / 2)
    gap = 6 - (cs ^ probe).area() / 0.1
    print(f"[verify] {name}: pinch gap at s={pinch_s[0] + pinch_len / 2:.1f} mm = {gap:.3f}")
    assert abs(gap - pinch) < 0.05
    crop = rrect(coupon_crop_x[0], coupon_crop_x[1], coupon_crop_y[0], coupon_crop_y[1])
    edge_ignore = crop - crop.offset(-3.0)  # crop corners and label notches
    for z in (plate_bottom_z + 0.4, plate_bottom_z + 2.0, ledge_bottom_z + 0.5, floor_top_z - 0.7):
        thin = thin_regions(m.slice(z), edge_ignore)
        print(f"[verify] {name}: z={z:+.2f} thin regions (<{minimum_wall_thickness} mm): {thin or 'none'}")
        assert not thin, thin


# --- Commands ------------------------------------------------------------------
def place_on_bed(parts: list[tuple[str, Manifold]]) -> list[tuple[str, Manifold, tuple[float, float, float]]]:
    """Template along the front, coupons rotated 90 deg in a row behind it."""
    placed = []
    name, tpl = parts[0]
    b = tpl.bounding_box()
    tx, ty = bed_margin - b[0], bed_margin - b[1]
    placed.append((name, tpl, (tx, ty, -b[2])))
    y_row = bed_margin + (b[4] - b[1]) + bed_gap
    x = bed_margin
    for name, m in parts[1:]:
        r = m.rotate([0, 0, 90])
        rb = r.bounding_box()
        placed.append((name, r, (x - rb[0], y_row - rb[1], -rb[2])))
        x += (rb[3] - rb[0]) + bed_gap
    for name, m, (px, py, pz) in placed:
        bb = m.bounding_box()
        x0, y0, x1, y1 = bb[0] + px, bb[1] + py, bb[3] + px, bb[4] + py
        print(f"[bed] {name}: X {x0:.1f}-{x1:.1f}  Y {y0:.1f}-{y1:.1f}  Z {bb[2] + pz:.2f}-{bb[5] + pz:.2f}")
        assert x0 >= bed_margin - 1e-6 and y0 >= bed_margin - 1e-6
        assert x1 <= bed_size - bed_margin and y1 <= bed_size - bed_margin, name
    return placed


def cmd_coupons(source: Manifold) -> None:
    tpl = build_template()
    report("center-check template", tpl)
    for z in (template_sheet / 2, template_sheet + template_lip / 2):
        thin = thin_regions(tpl.slice(z))
        print(f"[verify] template: z={z:.2f} thin regions (<{minimum_wall_thickness} mm): {thin or 'none'}")
        assert not thin, thin
    print(f"[verify] template: hole d={template_hole_d} flat +Y edge at y={template_hole_flat_y:.2f}; "
          f"nominal gaps -X/+X/-Y = {template_hole_d / 2 - 27.75:.2f} mm (55.5 mm puck), "
          f"+Y = {template_hole_flat_y - puck_center[1] - 27.75:.2f} mm; dy nominal term = {template_dy_nominal:.2f}")
    parts = [("center-check template (lip up, hole d66)", tpl)]
    for i, (bore, pinch) in enumerate(coupon_variants):
        name = f"coupon {i + 1} - bore {bore:.1f} pinch {pinch:.2f} ({i + 1} notch{'es' if i else ''})"
        m = build_coupon(source, i)
        verify_coupon(name, m, bore, pinch)
        parts.append((name, m))
    write_3mf(COUPON_3MF, place_on_bed(parts))
    print(f"[output] {COUPON_3MF}")


def cmd_plate(source: Manifold) -> None:
    built = build_plate(source)
    report("plate", built.solid)
    write_3mf(PLATE_3MF, [("iPhone Duo Plate 260 sloped magsafe", built.solid, source_bed_offset)])
    print(f"[output] {PLATE_3MF}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--coupons", action="store_true", help=f"write {COUPON_3MF.name}")
    ap.add_argument("--plate", action="store_true", help=f"write {PLATE_3MF.name}")
    args = ap.parse_args()
    if not (args.coupons or args.plate):
        ap.error("choose --coupons and/or --plate")
    from importlib.metadata import version
    print(f"[input] python={sys.executable} manifold3d={version('manifold3d')}")
    print(f"[input] source={SOURCE_3MF}")
    source = load_3mf(SOURCE_3MF)
    built = build_plate(source)
    print(f"[layout] old vents filled: {len(built.vents)}; grille slots: {len(built.slots)}; "
          f"back-edge exit notch from y={built.exit_y:.2f}")
    for x, y0, y1 in built.slots:
        print(f"[layout]   slot x={x:7.2f} y={y0:7.2f}..{y1:7.2f} len={y1 - y0:6.2f}")
    if args.coupons:
        cmd_coupons(source)
    if args.plate:
        cmd_plate(source)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
