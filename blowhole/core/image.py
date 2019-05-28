"""Classes for docker images."""

from dataclasses import field
from typing import List, Optional, Tuple

from pydantic.dataclasses import dataclass

from blowhole.core.config import ConfigModel


@dataclass
class ImageName(ConfigModel):
    """A class for docker image names, defining seperate repository and tags."""

    repository: str
    tag: Optional[str] = None

    def is_compatible(self, other: 'ImageName') -> bool:
        """Determine if an ImageName is compatible with another."""
        return (self == other) or (
            self.repository == other.repository
            and self.tag is None
        )

    @classmethod
    def from_str(cls, full_name: str) -> 'ImageName':
        """Take a fully qualified image name and returns an ImageName instance."""
        name = full_name.split(":")
        if len(name) == 1:
            return ImageName(name[0])
        elif len(name) == 2:
            return ImageName(name[0], name[1])
        else:
            raise ValueError("Image name cannot contain multiple tags.")

    def __str__(self) -> str:
        if self.tag is None:
            return self.repository
        else:
            return f"{self.repository}:{self.tag}"


@dataclass
class BuildRecipe(ConfigModel):
    """A set of instructions to build an image."""

    commands: List[str]

    def __str__(self) -> str:
        r = "BuildRecipe ["

        for c in self.commands:
            r += f"\n\t{c}"

        r += "\n]"

        return r


@dataclass
class RunRecipe:
    """A set of instructions to set up a running image."""

    script: List[str] = field(default_factory=list)
    ports: List[Tuple[int, int]] = field(default_factory=list)
    sockets: List[Tuple[str, str]] = field(default_factory=list)
    volumes: List[Tuple[str, str]] = field(default_factory=list)

    def __str__(self) -> str:
        r = "RunRecipe ("

        if self.script != []:
            r += f"\n\tscript={self.script},"

        if self.ports != []:
            r += f"\n\tports={self.ports},"

        if self.sockets != []:
            r += f"\n\tsockets={self.sockets},"

        if self.volumes != []:
            r += f"\n\tvolumes={self.volumes},"

        r += "\n)"

        return r
