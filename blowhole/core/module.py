"""Modules and associated components."""

from typing import List, Optional, Union

from blowhole.core.image import BuildRecipe, ImageName, RunRecipe


class Component:
    """An executable part of a module."""

    def __init__(
        self,
        recipe: Union[BuildRecipe, RunRecipe],
        compatible: Optional[List[ImageName]] = None,
        description: Optional[str] = None,
    ):
        self.recipe = recipe
        self.compatible = compatible
        self.description = description

    def should_run(self, source_image: ImageName) -> bool:
        """Should this component be executed for a given source image."""
        if self.compatible is None:
            return True
        else:
            for image in self.compatible:
                if image.is_compatible(source_image):
                    return True
            return False
