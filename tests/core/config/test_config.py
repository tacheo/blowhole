"""Test the config model."""

import os

import pytest
from pydantic import ValidationError
from pydantic.dataclasses import dataclass

from blowhole.core.config import ConfigModel

CURR_DIR = os.path.dirname(__file__)

BAD = os.path.join(CURR_DIR, 'files', 'bad.yml')
EMPTY = os.path.join(CURR_DIR, 'files', 'empty.yml')
VALID = os.path.join(CURR_DIR, 'files', 'valid.yml')


def test_initialisation() -> None:
    """Test ConfigModel initialisation with expected params."""
    ConfigModel()


def test_load_from_empty_file() -> None:
    """Test if we can load from a file."""
    with open(EMPTY) as fp:
        ConfigModel.load_from_file(fp)


@dataclass
class MockConfig(ConfigModel):
    """A mock config."""

    name: str


def test_load_from_file() -> None:
    """Test that we can load a yaml config."""
    with open(VALID) as fp:
        c = MockConfig.load_from_file(fp)

        assert type(c.name) is str
        assert c.name == "Bees"


def test_load_invalid_from_file() -> None:
    """Test that we can load a yaml config."""
    with pytest.raises(TypeError):
        with open(EMPTY) as fp:
            MockConfig.load_from_file(fp)

    with pytest.raises(ValidationError):
        with open(BAD) as fp:
            MockConfig.load_from_file(fp)
