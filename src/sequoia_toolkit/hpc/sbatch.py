"""Generation de scripts sbatch a partir d'options Python typees.

But : eviter que chaque projet reecrive son propre gabarit de script
Slurm avec des conventions differentes (noms de partitions, comptes de
calcul, chemins de logs, ...).
"""

from __future__ import annotations

from dataclasses import dataclass, field

_SBATCH_TEMPLATE = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --partition={partition}
#SBATCH --nodes={nodes}
#SBATCH --ntasks-per-node={ntasks_per_node}
#SBATCH --cpus-per-task={cpus_per_task}
{gpu_line}#SBATCH --time={time_limit}
#SBATCH --output={log_dir}/%x-%j.out
#SBATCH --error={log_dir}/%x-%j.err
{account_line}
set -euo pipefail

{modules_block}

{command}
"""


@dataclass
class SbatchOptions:
    """Options de generation d'un script sbatch.

    Champs volontairement proches du vocabulaire Slurm pour rester
    lisible par toute personne qui connait deja `sbatch`.
    """

    job_name: str
    command: str
    partition: str = "cpu"
    nodes: int = 1
    ntasks_per_node: int = 1
    cpus_per_task: int = 4
    time_limit: str = "01:00:00"
    log_dir: str = "logs"
    account: str | None = None
    gpus: int | None = None
    modules: list[str] = field(default_factory=list)


def render_sbatch_script(options: SbatchOptions) -> str:
    """Rend le contenu textuel d'un script sbatch a partir des options.

    Ne fait aucune I/O : a ecrire sur disque par l'appelant, ou a passer
    directement a `submit_job`.
    """
    gpu_line = f"#SBATCH --gres=gpu:{options.gpus}\n" if options.gpus else ""
    account_line = f"#SBATCH --account={options.account}" if options.account else ""
    modules_block = (
        "\n".join(f"module load {m}" for m in options.modules) if options.modules else ""
    )

    return _SBATCH_TEMPLATE.format(
        job_name=options.job_name,
        partition=options.partition,
        nodes=options.nodes,
        ntasks_per_node=options.ntasks_per_node,
        cpus_per_task=options.cpus_per_task,
        gpu_line=gpu_line,
        time_limit=options.time_limit,
        log_dir=options.log_dir,
        account_line=account_line,
        modules_block=modules_block,
        command=options.command,
    )
