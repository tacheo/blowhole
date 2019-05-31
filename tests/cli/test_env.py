"""Test the env cli."""

from os import path

from click.testing import CliRunner

from blowhole.cli.env import df, env

CURR_DIR = path.dirname(__file__)
ENV_VALID = path.join(CURR_DIR, "files", "env.yaml")

runner = CliRunner()


def test_env_endpoint() -> None:
    """Test that the env CLI endpoint does something."""
    result = runner.invoke(env)
    assert result.exit_code == 0


def test_env_df() -> None:
    """Test that the Dockerfile endpoint returns the right dockerfile."""
    result = runner.invoke(df, args=str(ENV_VALID))
    print(result.output)
    assert result.exit_code == 0
    assert result.output == "FROM ubuntu\n" \
        "RUN apt update && apt install zsh\n" \
        "CMD zsh\n\n"
