"""Base Configuration File."""

from typing import TextIO, Type, TypeVar

from pydantic import BaseModel, Extra
from pydantic.types import FilePath

T = TypeVar("T", bound='ConfigModel')


class ConfigModel(BaseModel):
    """A base configuration class."""

    file: FilePath

    class Config:
        """Configure the configuration model."""

        extra = Extra.forbid
        validate_assignment = True

    @classmethod
    def load_from_file(cls: Type[T], fp: TextIO) -> T:
        """Load a ConfigModel object from a file."""
        fp.read()
        return cls(
            file=fp.name,
        )
