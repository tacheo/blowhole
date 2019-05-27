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
    ):
        self.dockerfile_commands = dockerfile_commands

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BuildRecipe):
            raise NotImplementedError(
                "Cannot compare BuildRecipe to arbitrary object.",
            )
        return self.dockerfile_commands == other.dockerfile_commands

    def __str__(self) -> str:
        r = "BuildRecipe ["

        for c in self.dockerfile_commands:
            r += f"\n\t{c}"

        r += "\n]"

        return r

    def __repr__(self) -> str:
        return f"BuildRecipe({self.dockerfile_commands!r})"


class RunRecipe:
    """A set of instructions to set up a running image."""

    def __init__(
        self, *,
        script: List[str] = [],
        ports: List[Tuple[int, int]] = [],
        sockets: List[Tuple[str, str]] = [],
        volumes: List[Tuple[str, str]] = [],
    ):
        self.script = script
        self.ports = ports
        self.sockets = sockets
        self.volumes = volumes

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RunRecipe):
            raise NotImplementedError(
                "Cannot compare RunRecipe to arbitrary object.",
            )
        return all([
            self.script == other.script,
            self.ports == other.ports,
            self.sockets == other.sockets,
            self.volumes == other.volumes,
        ])

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

    def __repr__(self) -> str:
        return (
            "RunRecipe("
            f"script={self.script!r},"
            f"ports={self.ports!r},"
            f"sockets={self.sockets!r},"
            f"volumes={self.volumes!r}"
            ")"
        )
