"""Git helper run on the user's PC by auto_runner (uses the PC's own git login).

  git_sync.py check                 -> report git version / credential helper
  git_sync.py clone                 -> clone AdvancedPackaging into ../_github/
  git_sync.py pullbundle <file>     -> fetch commits from a git bundle into main
  git_sync.py push "<message>"      -> add -A, commit (if changes), push origin main
All git calls are non-interactive (no prompts) and time-limited.
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GH = ROOT / "_github"
REPO = Path(os.environ.get("AP_REPO", r"<local clone path>"))
URL = "https://github.com/HyeongjunKim00/AdvancedPackaging.git"
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")


def run(args, cwd=None, timeout=180):
    print(">", " ".join(args), flush=True)
    p = subprocess.run(args, cwd=cwd, env=ENV, capture_output=True, text=True, timeout=timeout)
    print(p.stdout[-4000:], p.stderr[-4000:], f"[exit {p.returncode}]", flush=True)
    return p.returncode


def main():
    cmd = sys.argv[1]
    if cmd == "unlock":
        lock = REPO / ".git" / "index.lock"
        if lock.exists():
            lock.unlink()
            print("removed", lock, flush=True)
        run(["git", "status", "--short"], cwd=REPO)
        run(["git", "log", "--oneline", "-3"], cwd=REPO)
        return
    if cmd == "check":
        run(["git", "--version"])
        run(["git", "config", "--global", "credential.helper"])
        run(["git", "config", "--global", "user.name"])
        run(["git", "config", "--global", "user.email"])
        run(["git", "ls-remote", "--heads", URL], timeout=60)
    elif cmd == "clone":
        GH.mkdir(exist_ok=True)
        if not REPO.exists():
            sys.exit(run(["git", "clone", URL, str(REPO)]))
        sys.exit(run(["git", "pull", "--ff-only"], cwd=REPO))
    elif cmd == "pullbundle":
        sys.exit(run(["git", "pull", "--ff-only", str((ROOT / sys.argv[2]).resolve()), "HEAD"], cwd=REPO))
    elif cmd == "push":
        msg = sys.argv[2]
        run(["git", "add", "-A"], cwd=REPO)
        if run(["git", "diff", "--cached", "--quiet"], cwd=REPO) != 0:
            if run(["git", "commit", "-m", msg], cwd=REPO) != 0:
                sys.exit(1)
        sys.exit(run(["git", "push", "origin", "HEAD:main"], cwd=REPO, timeout=300))


if __name__ == "__main__":
    main()
