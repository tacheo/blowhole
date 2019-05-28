"""Base Configuration File."""

from typing import TextIO, Type, TypeVar

from pydantic import Extra
from pydantic.dataclasses import dataclass
from ruamel.yaml import YAML

T = TypeVar("T", bound='ConfigModel')


@dataclass
class ConfigModel:
    """A base configuration class."""

    class Config:
        """Configure the configuration model."""

        extra = Extra.forbid
        validate_assignment = True

    @classmethod
    def load_from_file(cls: Type[T], fp: TextIO) -> T:
        """Load a ConfigModel object from a file."""
        yaml = YAML()

        data = yaml.load(fp)
        if data is None:
            return cls()
        else:
            return cls(  # type: ignore
                **data,
            )
