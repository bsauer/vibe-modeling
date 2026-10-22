# Workspace Git Setup

Recorded 2026-10-22 for the local clone under
`/Volumes/sandisk/project/3d-printing/cjtrowbridge/vibe-modeling`.

This document describes how **this workspace** is wired to GitHub. It is not a
generic fork recipe for every consumer of vibe-modeling.

## Remotes

| Remote | URL | Role |
|---|---|---|
| `origin` | `git@github.com:bsauer/vibe-modeling.git` | Personal fork. Default push target. `main` tracks `origin/main`. |
| `upstream` | `git@github.com:cjtrowbridge/vibe-modeling.git` | Canonical source repository. Fetch and merge/rebase from here. |

Web URLs:

- Fork: https://github.com/bsauer/vibe-modeling
- Upstream: https://github.com/cjtrowbridge/vibe-modeling

Fork parent on GitHub: `cjtrowbridge/vibe-modeling`.

## Submodule

| Path | URL | Notes |
|---|---|---|
| `agentic-pipelines/` | `https://github.com/cjtrowbridge/agentic-pipelines.git` | Required after clone. Host policy mounts it at `./agentic-pipelines`. |

Initialize if the directory is empty:

```bash
git submodule update --init --recursive agentic-pipelines
```

Do not edit files inside `agentic-pipelines/` for host work. Update the pointer
through the submodule-update playbook.

## Day-to-day commands

Pull latest from the personal fork (usual sync of this clone):

```bash
git fetch origin
git status -sb
```

Bring in new commits from the canonical upstream repo:

```bash
git fetch upstream
git log --oneline HEAD..upstream/main
git merge upstream/main
# or: git rebase upstream/main
```

Push local commits to the personal fork only (unless a different remote is
explicitly approved):

```bash
git push origin HEAD
```

Do not push to `upstream` unless the user explicitly authorizes a contribution
back to `cjtrowbridge/vibe-modeling` (typically via PR from the fork).

## History of this setup

1. Cloned from `cjtrowbridge/vibe-modeling`.
2. Initialized the `agentic-pipelines` submodule.
3. Fast-forwarded local `main` to then-current upstream.
4. Created the GitHub fork `bsauer/vibe-modeling`.
5. Renamed the former `origin` remote to `upstream` and set `origin` to the fork.
6. Committed and pushed local uv / iPhone Duo workspace changes to the fork
   (`e7f604c` on 2026-10-22).

## Agent expectations

- Treat `origin` as the writable remote for this workspace.
- Treat `upstream` as read-oriented sync from the original project.
- Prefer `docs/workspace-git-setup.md` over assumptions when remotes differ from
  a fresh single-remote clone.
- Commit and push still require explicit user approval unless already granted for
  that exact action (see root `AGENTS.md` and the commit playbooks).
