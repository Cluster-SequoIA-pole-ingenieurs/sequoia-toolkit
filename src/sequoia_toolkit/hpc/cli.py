"""Commande ``sequoia-job`` : un fichier job.yaml unique pour Slurm et PBS.

Exemples :
    sequoia-job detect
    sequoia-job render job.yaml                       # affiche le script genere
    sequoia-job render job.yaml --scheduler pbs       # ... pour un autre ordonnanceur
    sequoia-job submit job.yaml --set gpus=2 --wait
    sequoia-job status 12345
    sequoia-job cancel 12345
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

from sequoia_toolkit.core.exceptions import SequoiaError
from sequoia_toolkit.hpc.jobs import (
    cancel_job,
    get_job_status,
    render_script,
    submit_job,
    wait_for_job,
)
from sequoia_toolkit.hpc.schedulers import SUPPORTED, get_scheduler
from sequoia_toolkit.hpc.spec import JobSpec


def _load_spec(path: str, overrides: list[str]) -> JobSpec:
    data: Any = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SequoiaError(f"{path} doit contenir un dictionnaire YAML")
    for item in overrides:
        key, sep, raw = item.partition("=")
        if not sep:
            raise SequoiaError(f"--set attend cle=valeur, recu : {item!r}")
        data[key.strip()] = yaml.safe_load(raw)  # "2" -> 2, "[a, b]" -> liste
    return JobSpec.from_dict(data)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sequoia-job", description="Jobs HPC portables Slurm / PBS (sequoia-toolkit)."
    )
    parser.add_argument(
        "--scheduler",
        choices=SUPPORTED,
        help="impose l'ordonnanceur (sinon SEQUOIA_SCHEDULER, puis detection automatique)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("detect", help="affiche l'ordonnanceur qui sera utilise")

    for name, text in (("render", "affiche le script genere"), ("submit", "soumet le job")):
        cmd = sub.add_parser(name, help=text)
        cmd.add_argument("spec", help="fichier YAML de description du job")
        cmd.add_argument(
            "--set",
            action="append",
            default=[],
            metavar="CLE=VALEUR",
            help="surcharge un champ du fichier (repetable)",
        )
        if name == "submit":
            cmd.add_argument(
                "--workdir", default="jobs", help="ou conserver le script (defaut: jobs/)"
            )
            cmd.add_argument("--wait", action="store_true", help="attendre la fin du job")
            cmd.add_argument("--poll", type=float, default=15.0, help="intervalle de suivi (s)")
            cmd.add_argument(
                "--timeout",
                type=float,
                default=None,
                help="abandonner l'attente apres N secondes (le job continue)",
            )

    for name in ("status", "cancel"):
        cmd = sub.add_parser(name, help=f"{name} d'un job")
        cmd.add_argument("job_id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "detect":
            print(get_scheduler(args.scheduler).name)
        elif args.command == "render":
            print(render_script(_load_spec(args.spec, args.set), scheduler=args.scheduler), end="")
        elif args.command == "submit":
            spec = _load_spec(args.spec, args.set)
            job_id = submit_job(spec, scheduler=args.scheduler, workdir=args.workdir)
            print(job_id)
            if args.wait:
                status = wait_for_job(
                    job_id, scheduler=args.scheduler, poll_interval_seconds=args.poll
                )
                print(status.value)
                return 0 if status.value == "COMPLETED" else 1
        elif args.command == "status":
            print(get_job_status(args.job_id, scheduler=args.scheduler).value)
        elif args.command == "cancel":
            cancel_job(args.job_id, scheduler=args.scheduler)
    except (SequoiaError, OSError) as exc:
        print(f"sequoia-job : erreur : {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
