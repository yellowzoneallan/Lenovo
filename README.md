# Hybrid GPU Cluster – Intelligent Job Router

This project implements a **production-style hybrid AI infrastructure design** and a **Python-based job routing tool** that intelligently submits workloads to either Slurm or Kubernetes.

---

## 🧠 Overview

The system supports:
- Large-scale distributed training (Slurm)
- Low-latency inference (Kubernetes)
- Interactive workloads (Jupyter/VSCode via Kubernetes)
- Multi-tenancy with quotas
- Optional cloud bursting (AWS)

The included CLI tool (`hybrid-job-submit`) reads a YAML manifest and automatically routes jobs to the appropriate backend.


