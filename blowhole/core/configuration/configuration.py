"""
Base configuration class.

Handles loading and nice errors.
"""

from abc import ABCMeta
from typing import TextIO, Type, TypeVar, cast

from ruamel.yaml import YAML
from typesystem import Schema


class ConfigurationError(Exception):
    """Bad configarion."""


T = TypeVar("T", bound='Configuration')


class Configuration(Schema, metaclass=ABCMeta):
    """Base configuration class."""

    @classmethod
    def load_file(cls: Type[T], fp: TextIO) -> T:
        """Load the configuration from a file-like object."""
        yaml = YAML()
        data = yaml.load(fp)

        return cast(T, cls.validate(data))
