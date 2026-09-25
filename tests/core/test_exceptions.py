from sequoia_toolkit.core.exceptions import SequoiaConfigError, SequoiaError


def test_config_error_is_a_sequoia_error():
    assert issubclass(SequoiaConfigError, SequoiaError)
