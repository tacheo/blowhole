"""Classes for docker images."""

from dataclasses import field
from typing import List, Optional, Set, Tuple, TypeVar

from pydantic.dataclasses import dataclass

from blowhole.core.config import ConfigModel


@dataclass
class ImageName(ConfigModel):
    """A class for docker image names, defining separate repository and tags."""

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

    commands: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        r = "BuildRecipe ["

        for c in self.commands:
            r += f"\n\t{c}"

        r += "\n]"

        return r

    @property
    def build_str(self) -> str:
        """The string to insert into the Dockerfile."""
        r = ""

        for c in self.commands:
            r += f"{c}\n"

        return r

    def __add__(self, other: 'BuildRecipe') -> 'BuildRecipe':
        return BuildRecipe(self.commands + other.commands)

    def __iadd__(self, other: 'BuildRecipe') -> 'BuildRecipe':
        self.commands += other.commands
        return self


T = TypeVar('T', Tuple[str, str], Tuple[int, int])


def combine(first: Set[T], second: Set[T]) -> Set[T]:
    """Combine two sets of tuples, prioritising the second."""
    result = second.copy()
    for pf in first:
        include = True
        for pr in result:
            if pf[0] == pr[0]:
                include = False
                break
            if pf[1] == pr[1]:
                include = False
                break
        if include:
            result.add(pf)
    return result


@dataclass
class RunRecipe(ConfigModel):
    """A set of instructions to set up a running image."""

    script: List[str] = field(default_factory=list)
    ports: Set[Tuple[int, int]] = field(default_factory=set)
    sockets: Set[Tuple[str, str]] = field(default_factory=set)
    volumes: Set[Tuple[str, str]] = field(default_factory=set)

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
