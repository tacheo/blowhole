"""Modules and associated components."""

from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from blowhole.core.image import BuildRecipe, ImageName, RunRecipe


@dataclass
class Component:
    """An executable part of a module."""

    recipe: Union[BuildRecipe, RunRecipe]
    compatible: Optional[List[ImageName]] = None
    description: Optional[str] = None

    def should_run(self, source_image: ImageName) -> bool:
        """Should this component be executed for a given source image."""
        if self.compatible is None:
            return True
        else:
            for image in self.compatible:
                if image.is_compatible(source_image):
                    return True
            return False


class Module:
    """An individual pluggable component of an image."""

    def __init__(
        self,
        name: str,
        components: List[Component],
        description: Optional[str] = None,
    ):
        self.name = name
        self.components = components
        self.description = description
