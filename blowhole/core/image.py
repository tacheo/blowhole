"""Classes for docker images."""

from typing import List, Optional, Tuple


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

    def __repr__(self) -> str:
        if self.tag is None:
            return f"ImageName({self.repository!r})"
        else:
            return f"ImageName({self.repository!r}, {self.tag!r})"


class BuildRecipe:
    """A set of instructions to build an image."""

    def __init__(
        self,
        dockerfile_commands: List[str],
        name: Optional[ImageName] = None,
    ):
        self.dockerfile_commands = dockerfile_commands
        self.name = name

    def __str__(self) -> str:
        if self.name is None:
            r = "BuildRecipe ["
        else:
            r = f"BuildRecipe {self.name} ["

        for c in self.dockerfile_commands:
            r += f"\n\t{c}"

        r += "\n]"

        return r

    def __repr__(self) -> str:
        if self.name is None:
            return f"BuildRecipe({self.dockerfile_commands!r})"
        else:
            return f"BuildRecipe({self.dockerfile_commands!r}, {self.name!r})"


class RunRecipe:
    """A set of instructions to set up a running image."""

    def __init__(
        self,
        script: List[str] = [],
        ports: List[Tuple[int, int]] = [],
        sockets: List[Tuple[str, str]] = [],
        volumes: List[Tuple[str, str]] = [],
    ):
        self.script = script
        self.ports = ports
        self.sockets = sockets
        self.volumes = volumes
