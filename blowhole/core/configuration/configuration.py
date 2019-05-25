"""
Base configuration class.

Handles loading and nice errors.
"""

from abc import ABCMeta
from typing import TextIO, Type

from typesystem import Schema, tokenize_yaml, validate_with_positions


class Configuration(Schema, metaclass=ABCMeta):
    """Base configuration class."""

    @classmethod
    def load_file(cls, fp: TextIO) -> Type['Configuration']:
        """Load the configuration from a file-like object."""
        data = fp.read()
        token = tokenize_yaml(data)

        # The below type is ignored due to limitations with Typesystem.
        return validate_with_positions(token=token, validator=cls)  # type: ignore
