from sequoia_toolkit.ml import start_run
from sequoia_toolkit.ml.experiment import ExperimentRun


class _RecordingBackend:
    def __init__(self):
        self.params = {}
        self.metrics = []
        self.artifacts = []

    def log_param(self, key, value):
        self.params[key] = value

    def log_metric(self, key, value, *, step=None):
        self.metrics.append((key, value, step))

    def log_artifact(self, path):
        self.artifacts.append(path)


def test_start_run_yields_experiment_run_with_default_backend():
    with start_run("test_run") as run:
        assert isinstance(run, ExperimentRun)
        run.log_param("lr", 0.001)
        run.log_metric("accuracy", 0.9)


def test_start_run_uses_custom_backend():
    backend = _RecordingBackend()

    with start_run("test_run", backend=backend) as run:
        run.log_param("batch_size", 32)
        run.log_metric("loss", 0.5, step=1)
        run.log_artifact("model.pt")

    assert backend.params == {"batch_size": 32}
    assert backend.metrics == [("loss", 0.5, 1)]
    assert backend.artifacts == ["model.pt"]


def test_run_params_are_tracked_locally():
    with start_run("test_run") as run:
        run.log_param("epochs", 10)
        assert run.params == {"epochs": 10}
