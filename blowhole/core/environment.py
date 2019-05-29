"""Build containers and images."""

from typing import Optional

from pydantic.dataclasses import dataclass

from blowhole.core.image import BuildRecipe, RunRecipe


@dataclass
class EnvironmentRecipe:
    """Can be built into a container or image."""

    build: BuildRecipe
    run: RunRecipe
    name: Optional[str]
