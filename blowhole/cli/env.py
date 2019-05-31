"""CLI interface for Blowhole Environments."""

from typing import TextIO

import click

from blowhole.core.environment import EnvironmentDefinition


@click.group("env")
def env() -> None:
    """
    Blowhole.

    Manage environments.
    """


@env.command()
@click.argument('envdef', type=click.File('rb'), default='blowhole.yml')
def df(envdef: TextIO) -> None:
    """Output the generated dockerfile for the given environment definition file."""
    env = EnvironmentDefinition.load_from_file(envdef)

    recipe = env.recipe

    click.echo(recipe.dockerfile_str)
