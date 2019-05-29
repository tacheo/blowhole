"""Build containers and images."""

from typing import List, Optional

from pydantic.dataclasses import dataclass

from blowhole.core.config import ConfigModel
from blowhole.core.image import BuildRecipe, RunRecipe
from blowhole.core.module import Module


@dataclass
class EnvironmentRecipe:
    """Can be built into a container or image."""

    build: BuildRecipe
    run: RunRecipe
    name: Optional[str] = None


@dataclass
class EnvironmentDefinition(ConfigModel):
    """A definition of how to construct an envrionment."""

    modules: List[Module]
    name: Optional[str] = None

    @property
    def recipe(self) -> EnvironmentRecipe:
        """Create a buildable Recipe from this definition."""
        current_image = None
        build = BuildRecipe()
        run = RunRecipe()

        for m in self.modules:
            for c in m.components:
                if c.should_run(current_image):
                    if isinstance(c.recipe, BuildRecipe):
                        build += c.recipe
                    elif isinstance(c.recipe, RunRecipe):
                        run += c.recipe
                    if c.results is not None:
                        current_image = c.results

        return EnvironmentRecipe(
            build=build,
            run=run,
            name=self.name,
        )
