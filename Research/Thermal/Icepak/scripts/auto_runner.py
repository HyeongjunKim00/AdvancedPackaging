"""Unattended queue runner for P11 Icepak scripts.

Start once in PowerShell and leave the window open:
    py -3.12 <project>\\RunScript\\auto_runner.py

It polls RunScript\\queue\\ for *.request files. Each request is one line:
    <script filename inside RunScript> [args...]
Only .py files located directly in RunScript\\ are executed. Output goes to
Runs\\_runner_logs\\<request>.log, and a <request>.done file with the exit code
is written when the run finishes. Stop with Ctrl+C or by creating
queue\\STOP.
"""

import shlex
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
QUEUE = SCRIPT_DIR / "queue"
LOGS = SCRIPT_DIR.parent / "Runs" / "_runner_logs"
POLL_S = 10


def main():
    QUEUE.mkdir(exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    heartbeat = QUEUE / "runner_heartbeat.txt"
    print(f"Watching {QUEUE} (Ctrl+C to stop)", flush=True)
    while True:
        heartbeat.write_text(datetime.now().isoformat(), encoding="utf-8")
        if (QUEUE / "STOP").exists():
            print("STOP file found; exiting.", flush=True)
            return
        requests = sorted(QUEUE.glob("*.request"))
        for req in requests:
            done = req.with_suffix(".done")
            if done.exists():
                continue
            parts = shlex.split(req.read_text(encoding="utf-8").strip(), posix=False)
            if not parts:
                done.write_text("REJECTED empty request", encoding="utf-8")
                continue
            script = (SCRIPT_DIR / parts[0]).resolve()
            if script.parent != SCRIPT_DIR or script.suffix != ".py" or not script.exists():
                done.write_text(f"REJECTED {parts[0]}", encoding="utf-8")
                continue
            log = LOGS / f"{req.stem}.log"
            print(f"[{datetime.now():%H:%M:%S}] running {req.name}: {parts}", flush=True)
            (QUEUE / f"{req.stem}.running").write_text(str(log), encoding="utf-8")
            with log.open("w", encoding="utf-8") as fh:
                proc = subprocess.run(
                    [sys.executable, "-u", str(script)] + parts[1:],
                    stdout=fh, stderr=subprocess.STDOUT, cwd=str(SCRIPT_DIR),
                )
            (QUEUE / f"{req.stem}.running").unlink(missing_ok=True)
            done.write_text(f"EXIT {proc.returncode}\nLOG {log}", encoding="utf-8")
            print(f"[{datetime.now():%H:%M:%S}] {req.name} exit {proc.returncode}", flush=True)
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
