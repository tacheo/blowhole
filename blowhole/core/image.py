"""Classes for docker images."""

from functools import total_ordering
from typing import List, Optional, Tuple


@total_ordering
class ImageName:
    """A class for docker image names, defining seperate repository and tags."""

    repository: str
    tag: Optional[str]

    def __init__(self, repository: str, tag: Optional[str] = None) -> None:
        self.repository = repository
        self.tag = tag

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ImageName):
            raise NotImplementedError(
                "Cannot compare ImageName to arbitrary object.",
            )
        return self.repository == other.repository and self.tag == other.tag

    def __gt__(self, other: 'ImageName') -> bool:
        return self.tag is None and other.tag is not None and \
            self.repository == other.repository

    @classmethod
    def from_str(cls, full_name: str) -> 'ImageName':
        """Takes a full image name string and returns equivalent ImageName."""
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
            return self.repository + ":" + self.tag


class BuildRecipe:
    """A set of instructions to build an image."""

    def __init__(
        self,
        dockerfile_commands: List[str],
        name: Optional[ImageName] = None,
    ):
        self.dockerfile_commands = dockerfile_commands
        self.name = name


class RunRecipe:
    """A set of instructions to set up a running image."""

    def __init__(
        self,
        script: Optional[List[str]] = None,
        ports: Optional[List[Tuple[int, int]]] = None,
        sockets: Optional[List[Tuple[str, str]]] = None,
        volumes: Optional[List[Tuple[str, str]]] = None,
    ):
        self.script = script
        self.sockets = sockets
        self.volumes = volumes
