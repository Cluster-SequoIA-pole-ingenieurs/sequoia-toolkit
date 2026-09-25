"""Adaptateur Slurm (sbatch / squeue / sacct / scontrol / scancel)."""

from __future__ import annotations

from pathlib import Path

from sequoia_toolkit.hpc.schedulers.base import Scheduler
from sequoia_toolkit.hpc.spec import JobSpec, JobStatus

# Etats Slurm -> etats normalises. Les etats absents donnent UNKNOWN.
_STATES: dict[str, JobStatus] = {
    "PENDING": JobStatus.PENDING,
    "CONFIGURING": JobStatus.PENDING,
    "REQUEUED": JobStatus.PENDING,
    "REQUEUE_HOLD": JobStatus.PENDING,
    "RESV_DEL_HOLD": JobStatus.PENDING,
    "SUSPENDED": JobStatus.PENDING,
    "RUNNING": JobStatus.RUNNING,
    "COMPLETING": JobStatus.RUNNING,
    "STAGE_OUT": JobStatus.RUNNING,
    "COMPLETED": JobStatus.COMPLETED,
    "FAILED": JobStatus.FAILED,
    "TIMEOUT": JobStatus.FAILED,
    "OUT_OF_MEMORY": JobStatus.FAILED,
    "NODE_FAIL": JobStatus.FAILED,
    "BOOT_FAIL": JobStatus.FAILED,
    "DEADLINE": JobStatus.FAILED,
    "PREEMPTED": JobStatus.FAILED,
    "CANCELLED": JobStatus.CANCELLED,
}


def _to_status(raw: str) -> JobStatus:
    # "CANCELLED by 1234" -> "CANCELLED" ; "CANCELLED+" (sacct) -> "CANCELLED"
    token = raw.strip().split()[0].rstrip("+").upper() if raw.strip() else ""
    return _STATES.get(token, JobStatus.UNKNOWN)


class SlurmScheduler(Scheduler):
    name = "slurm"
    family = "slurm"
    submit_binary = "sbatch"
    script_suffix = ".sbatch"

    def header(self, spec: JobSpec) -> list[str]:
        d = [f"--job-name={spec.job_name}"]
        if spec.queue:
            d.append(f"--partition={spec.queue}")
        d += [
            f"--nodes={spec.nodes}",
            f"--ntasks-per-node={spec.ntasks_per_node}",
            f"--cpus-per-task={spec.cpus_per_task}",
        ]
        memory = spec.memory_per_node
        if memory:
            d.append(f"--mem={memory.value}{memory.unit}")
        if spec.gpus:
            d.append(f"--gres=gpu:{spec.gpus}")
        d += [
            f"--time={spec.time_limit}",
            f"--output={spec.log_dir}/%x-%j.out",
            f"--error={spec.log_dir}/%x-%j.err",
        ]
        if spec.account:
            d.append(f"--account={spec.account}")
        d += spec.directives_for(self.family)
        return [f"#SBATCH {directive}" for directive in d]

    def runtime_exports(self, spec: JobSpec) -> list[str]:
        # Slurm lance deja le job dans le repertoire de soumission.
        return [
            "export SEQUOIA_JOB_SCHEDULER=slurm",
            'export SEQUOIA_JOB_ID="$SLURM_JOB_ID"',
            'export SEQUOIA_JOB_SUBMIT_DIR="$SLURM_SUBMIT_DIR"',
        ]

    def submit_args(self, script_path: Path) -> list[str]:
        return ["sbatch", "--parsable", str(script_path)]

    def parse_job_id(self, stdout: str) -> str:
        # --parsable : "12345" ou "12345;nom_du_cluster"
        return stdout.strip().split(";")[0]

    def cancel_args(self, job_id: str) -> list[str]:
        return ["scancel", job_id]

    def status(self, job_id: str) -> JobStatus:
        # 1. Job encore dans la file ?
        result = self._run(["squeue", "-j", job_id, "-h", "-o", "%T"])
        if result.returncode == 0 and result.stdout.strip():
            return _to_status(result.stdout)

        # 2. Job termine : comptabilite (si activee sur le cluster).
        result = self._run(["sacct", "-j", job_id, "-X", "-n", "-P", "-o", "State"])
        if result.returncode == 0 and result.stdout.strip():
            return _to_status(result.stdout.strip().splitlines()[0])

        # 3. Sans comptabilite : scontrol garde les jobs termines recemment (MinJobAge).
        result = self._run(["scontrol", "show", "job", job_id, "-o"])
        if result.returncode == 0:
            for item in result.stdout.split():
                if item.startswith("JobState="):
                    return _to_status(item.split("=", 1)[1])
        return JobStatus.UNKNOWN
