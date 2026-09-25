"""Simulateur de commandes d'ordonnanceur : enregistre les appels et rejoue des
sorties preparees, pour tester sans Slurm ni PBS installes."""

from __future__ import annotations

import subprocess

import pytest

from sequoia_toolkit.hpc.schedulers.base import Scheduler


class FakeRunner:
    def __init__(self) -> None:
        self.calls: list[list[str]] = []
        self.responses: dict[str, list[tuple[int, str, str]]] = {}

    def on(self, binary: str, stdout: str = "", returncode: int = 0, stderr: str = "") -> None:
        self.responses.setdefault(binary, []).append((returncode, stdout, stderr))

    def __call__(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        self.calls.append(args)
        queue = self.responses.get(args[0], [])
        code, out, err = queue.pop(0) if queue else (1, "", f"{args[0]}: pas de reponse simulee")
        return subprocess.CompletedProcess(args, code, out, err)

    def binaries(self) -> list[str]:
        return [call[0] for call in self.calls]


@pytest.fixture
def runner(monkeypatch: pytest.MonkeyPatch) -> FakeRunner:
    fake = FakeRunner()
    monkeypatch.setattr(Scheduler, "_run", staticmethod(fake))
    return fake
