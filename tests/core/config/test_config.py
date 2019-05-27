"""Test the config model."""

import os
from pathlib import PurePath

import pydantic
import pytest

from blowhole.core.config import ConfigModel

CURR_DIR = os.path.dirname(__file__)

BAD = os.path.join(CURR_DIR, 'files', 'bad.yml')
EMPTY = os.path.join(CURR_DIR, 'files', 'empty.yml')


def test_initialisation() -> None:
    """Test ConfigModel initialisation with expected params."""
    c = ConfigModel(file=EMPTY)
    assert isinstance(c.file, PurePath)
    assert c.file.exists()


def test_initialisation_with_bad_type() -> None:
    """Test ConfigModel initialisation with bad param types."""
    with pytest.raises(pydantic.ValidationError):
        ConfigModel(file=1)


def test_initialisation_with_wrong_params() -> None:
    """Test config model initialisation with the wrong number of params."""
    with pytest.raises(pydantic.ValidationError):
        ConfigModel(file=EMPTY, bees=True, number=42)

    with pytest.raises(pydantic.ValidationError):
        ConfigModel()


def test_initialisation_with_bad_file_path() -> None:
    """Test config model initialisation with a file that is non-existent."""
    # No such file.
    with pytest.raises(pydantic.ValidationError):
        ConfigModel(file=BAD)

    # Not a file.
    with pytest.raises(pydantic.ValidationError):
        ConfigModel(file=os.path.join('not', 'a', 'file'))


def test_validation_of_assignment() -> None:
    """Test that we validate the assignment of attributes."""
    c = ConfigModel(file=EMPTY)
    # We ignore the next line, as we are deliberately breaking types
    # to see if it throws an error.
    c.file = EMPTY  # type: ignore

    with pytest.raises(pydantic.ValidationError):
        # We ignore the next line, as we are deliberately breaking types
        # to see if it throws an error.
        c.file = BAD  # type: ignore
