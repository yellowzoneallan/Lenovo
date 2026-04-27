import subprocess
import re


def slurm_queue_depth():
    try:
        out = subprocess.check_output(["squeue", "-h"]).decode()
        return len(out.strip().splitlines())
    except Exception:
        return 0


def submit_slurm(config):
    cmd = [
        "sbatch",
        f"--gres=gpu:{config['gpus']}",
        f"--time={config['duration_hours']}:00:00",
        "--wrap",
        config["command"],
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    match = re.search(r"Submitted batch job (\d+)", result.stdout)
    job_id = match.group(1) if match else "unknown"

    return {
        "backend": "slurm",
        "job_id": job_id,
        "expected_start": "queue-based",
        "status": "submitted",
    }
