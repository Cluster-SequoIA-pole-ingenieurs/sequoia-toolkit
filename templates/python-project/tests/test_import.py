"""Source import smoke check; this does not validate application or scientific behavior."""

from importlib import import_module


def test_source_is_importable() -> None:
    import_module("sequoia_project")
