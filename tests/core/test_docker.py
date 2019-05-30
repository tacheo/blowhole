"""Test our docker wrappers."""

import pytest

from blowhole.core.docker import DockerException, whale_call


def test_whale_call() -> None:
    """Test successful whale calls."""
    @whale_call
    def add(x: int, y: int) -> int:
        return x + y

    assert add(17, 3) == 20


def test_whale_call_filenotfounderror() -> None:
    """Test FileNotFoundErrors in whale calls."""
    @whale_call
    def fail() -> None:
        raise FileNotFoundError

    with pytest.raises(DockerException):
        fail()


def test_whale_call_othererror() -> None:
    """Test other Errors in whale calls."""
    @whale_call
    def fail() -> None:
        raise ValueError

    with pytest.raises(ValueError):
        fail()
