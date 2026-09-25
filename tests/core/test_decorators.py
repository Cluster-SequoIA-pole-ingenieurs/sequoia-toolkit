import pytest

from sequoia_toolkit.core.decorators import retry, timeit


def test_timeit_returns_original_value():
    @timeit
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_retry_eventually_succeeds():
    calls = {"n": 0}

    @retry(times=3, delay_seconds=0)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 2:
            raise ValueError("echec temporaire")
        return "ok"

    assert flaky() == "ok"
    assert calls["n"] == 2


def test_retry_raises_after_exhausting_attempts():
    @retry(times=2, delay_seconds=0)
    def always_fails():
        raise ValueError("echec permanent")

    with pytest.raises(ValueError):
        always_fails()
