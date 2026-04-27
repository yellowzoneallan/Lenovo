import subprocess
import uuid
import json


def submit_k8s(config):
    job_name = f"job-{uuid.uuid4()}"

    job = {
        "apiVersion": "batch/v1",
        "kind": "Job",
        "metadata": {"name": job_name},
        "spec": {
            "template": {
                "spec": {
                    "containers": [
                        {
                            "name": "job",
                            "image": config["image"],
                            "command": ["/bin/sh", "-c", config["command"]],
                            "resources": {"limits": {"nvidia.com/gpu": config["gpus"]}},
                        }
                    ],
                    "restartPolicy": "Never",
                }
            }
        },
    }

    with open("job.json", "w") as f:
        json.dump(job, f)

    subprocess.run(["kubectl", "apply", "-f", "job.json"])

    return {
        "backend": "kubernetes",
        "job_id": job_name,
        "expected_start": "near-immediate",
        "status": "submitted",
    }
