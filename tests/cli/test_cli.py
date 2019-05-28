"""Test the cli endpoint and basic commands."""

from click.testing import CliRunner

from blowhole import __version__
from blowhole.cli.cli import cli, version

runner = CliRunner()


def test_cli_endpoint() -> None:
    """Test that the CLI endpoint does something."""
    result = runner.invoke(cli)
    assert result.exit_code == 0


def test_cli_version() -> None:
    """Test that the CLI endpoint returns the right version."""
    result = runner.invoke(version)
    assert result.exit_code == 0
    assert result.output == f"Blowhole v{__version__}\n"
