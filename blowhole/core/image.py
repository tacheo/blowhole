"""Classes for docker images."""

from typing import Optional


class ImageName:
    """A class for docker image names, defining seperate repository and tags."""

    repository: str
    tag: Optional[str]

    def __init__(self, repository: str, tag: Optional[str] = None) -> None:
        self.repository = repository
        self.tag = tag
