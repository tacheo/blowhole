"""CLI interface for Blowhole Environments."""

import click


@click.group("env")
def env() -> None:
    """
    Blowhole.

    Manage environments.
    """
