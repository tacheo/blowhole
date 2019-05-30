"""Main CLI interface for Blowhole."""

import click

from blowhole import __version__
from blowhole.cli.env import env


@click.group('bh', invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """
    Blowhole.

    A tool for creating, managing, and using docker-based development environments.
    """
    if ctx.invoked_subcommand is None:
        click.echo('Unable to find blowhole configuration.', err=True)
        click.echo('Nothing is implemented here.', err=True)


@cli.command()
def version() -> None:
    """Display the version."""
    click.echo(f"Blowhole v{__version__}")


cli.add_command(env)
