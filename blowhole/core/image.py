"""Classes for docker images."""

from typing import Optional


class ImageName:
    """A class for docker image names, defining seperate repository and tags."""

    repository: str
    tag: Optional[str]

    def __init__(self, repository: str, tag: Optional[str] = None) -> None:
        self.repository = repository
        self.tag = tag

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
