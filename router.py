from quotas import check_quota
from slurm import submit_slurm, slurm_queue_depth
from k8s import submit_k8s


def route_job(config):
    check_quota(config)

    jt = config["job_type"]

    # Advanced policy: burst if queue too long
    if jt == "training" and slurm_queue_depth() > 50:
        return {"decision": "burst-to-cloud"}

    if jt == "training":
        return submit_slurm(config)
    elif jt in ["inference", "interactive"]:
        return submit_k8s(config)
    else:
        raise Exception("Invalid job type")
