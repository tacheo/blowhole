"""Test the config model."""

import os
from pathlib import Path

import pydantic
import pytest

from blowhole.core.config import ConfigModel

CURR_DIR = os.path.dirname(__file__)

BAD = os.path.join(CURR_DIR, 'files', 'bad.yml')
EMPTY = os.path.join(CURR_DIR, 'files', 'empty.yml')


def test_initialisation() -> None:
    """Test ConfigModel initialisation with expected params."""
    c = ConfigModel(file=EMPTY)
    assert isinstance(c.file, Path)
    assert c.file.exists()


def test_initialisation_with_bad_type() -> None:
    """Test ConfigModel initialisation with bad param types."""
    with pytest.raises(pydantic.ValidationError) as error:
        ConfigModel(file=1)

    assert len(error.value.errors()) == 1


def test_initialisation_with_wrong_params() -> None:
    """Test config model initialisation with the wrong number of params."""
    with pytest.raises(pydantic.ValidationError) as error:
        ConfigModel(file=EMPTY, bees=True, number=42)

    assert len(error.value.errors()) == 2

    with pytest.raises(pydantic.ValidationError) as error:
        ConfigModel()

    assert len(error.value.errors()) == 1


def test_initialisation_with_bad_file_path() -> None:
    """Test config model initialisation with a file that is non-existent."""
    # No such file.
    with pytest.raises(pydantic.ValidationError) as error:
        ConfigModel(file=BAD)

    assert len(error.value.errors()) == 1

    # Not a file.
    with pytest.raises(pydantic.ValidationError) as error:
        ConfigModel(file=os.path.join('not', 'a', 'file'))

    assert len(error.value.errors()) == 1


def test_validation_of_assignment() -> None:
    """Test that we validate the assignment of attributes."""
    c = ConfigModel(file=EMPTY)
    c.file = EMPTY

    with pytest.raises(pydantic.ValidationError):
        c.file = BAD