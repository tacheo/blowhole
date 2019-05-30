"""Test environment classes."""

from os import path

import pytest
from pydantic import ValidationError

from blowhole.core.environment import EnvironmentDefinition, EnvironmentRecipe
from blowhole.core.image import BuildRecipe, ImageName, RunRecipe
from blowhole.core.module import Component, Module

CURR_DIR = path.dirname(__file__)

YAML_EMPTY = path.join(CURR_DIR, "files", "empty.yaml")

ENV_VALID = path.join(CURR_DIR, "files", "env_valid.yaml")
ENV_INVALID = path.join(CURR_DIR, "files", "env_invalid.yaml")


def test_environmentrecipe_instantiation() -> None:
    """Test creating Environment Recipes."""
    EnvironmentRecipe(BuildRecipe(), RunRecipe(), "potato")
    EnvironmentRecipe(
        build=BuildRecipe(),
        run=RunRecipe(),
        name=None,
    )


def test_environmentdefinition_instantiation() -> None:
    """Test creating Environment Definitions."""
    EnvironmentDefinition([])
    EnvironmentDefinition([], "Wow!")


def test_environmentdefinition_load_empty() -> None:
    """Test loading an empty file as an environment definition."""
    with pytest.raises(TypeError):
        with open(YAML_EMPTY) as fp:
            EnvironmentDefinition.load_from_file(fp)


def test_environmentdefinition_load_invalid() -> None:
    """Test loading an invalid environment definition."""
    with pytest.raises(ValidationError):
        with open(ENV_INVALID) as fp:
            EnvironmentDefinition.load_from_file(fp)


def test_environmentdefinition_load_valid() -> None:
    """Test loading Environment Definition from file."""
    m1 = Module(
        name="ubuntu",
        components=[Component(
            recipe=BuildRecipe(commands=["FROM ubuntu"]),
            results=ImageName("ubuntu"),
        )],
    )

    m2 = Module(
        name="zsh",
        components=[Component(
            recipe=BuildRecipe(commands=["RUN apt update && apt install zsh"]),
            compatible=[ImageName("ubuntu"), ImageName("debian")],
            description="Installs zsh using apt.",
        ), Component(
            recipe=BuildRecipe(commands=["RUN pacman -S zsh"]),
            compatible=[ImageName("arch"), ImageName("manjaro")],
            description="Installs zsh using pacman.",
        ), Component(
            recipe=BuildRecipe(commands=["CMD zsh"]),
            description="Use zsh as the entry command.",
        ), Component(
            recipe=RunRecipe(ports=[(3000, 3000), (8080, 8080)]),
        )],
    )

    env_valid = EnvironmentDefinition(
        name="example-environment",
        modules=[m1, m2],
    )

    with open(ENV_VALID) as fp:
        assert EnvironmentDefinition.load_from_file(fp) == env_valid


def test_environmentdefinition_recipe() -> None:
    """Test converting environment definitions to environment recipes."""
    r = EnvironmentRecipe(
        name="example-environment",
        build=BuildRecipe(
            commands=[
                "FROM ubuntu",
                "RUN apt update && apt install zsh",
                "CMD zsh",
            ],
        ),
        run=RunRecipe(
            ports={
                (3000, 3000),
                (8080, 8080),
            },
        ),
    )

    with open(ENV_VALID) as fp:
        assert EnvironmentDefinition.load_from_file(fp).recipe == r


def test_environmentdefinition_dockerfile_str() -> None:
    """Test outputting dockerfiles from environment definitions."""
    d = (
        "FROM ubuntu\n"
        "RUN apt update && apt install zsh\n"
        "CMD zsh\n"
    )

    with open(ENV_VALID) as fp:
        assert EnvironmentDefinition.load_from_file(fp).recipe.dockerfile_str == d
