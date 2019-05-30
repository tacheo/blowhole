"""Test the env cli."""

from click.testing import CliRunner

from blowhole.cli.env import env

runner = CliRunner()


def test_env_endpoint() -> None:
    """Test that the env CLI endpoint does something."""
    result = runner.invoke(env)
    assert result.exit_code == 0
