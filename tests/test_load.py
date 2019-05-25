"""Test that it is not completely broken."""


def test_load_module() -> None:
    """Test that we can load the module."""
    import blowhole  # noqa: F401, F403
