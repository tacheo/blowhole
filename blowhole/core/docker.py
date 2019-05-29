"""Docker wrapper."""

from functools import wraps
from typing import Callable, TypeVar

from .exception import BlowholeException


class DockerException(BlowholeException):
    """An error occurred with Docker."""


RT = TypeVar('RT')


def whale_call(f: Callable[..., RT]) -> Callable[..., RT]:  # type: ignore
    """Decorator to catch and re-throw docker errors in a friendly manner."""
    @wraps(f)
    def wrapper(*args, **kwargs):  # type: ignore
        try:
            return f(*args, **kwargs)
        except FileNotFoundError:
            raise DockerException(
                "Unable to communicate with the docker daemon.",
            ) from None

    return wrapper


class DockerManager:
    """Manages and wraps interfacing with docker."""
