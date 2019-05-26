"""Test module classes."""

from blowhole.core.image import BuildRecipe, ImageName, RunRecipe
from blowhole.core.module import Component, Module


def test_component_initialisation() -> None:
    """Test creating components."""
    Component(BuildRecipe(["RUN cd ."]))
    Component(
        RunRecipe(["a", "b"]),
        [ImageName.from_str("a/b:c"), ImageName("qwerty", "uiop")],
        "does absolutely nothing",
    )


def test_component_should_run() -> None:
    """Test whether components should be executed."""
    c1 = Component(RunRecipe(), [ImageName("ubuntu"), ImageName("debian", "stretch")])
    c2 = Component(BuildRecipe(["FROM nixos"]))

    i1 = ImageName("ubuntu")
    i2 = ImageName("ubuntu", "18.04")
    i3 = ImageName("debian")
    i4 = ImageName("debian", "stretch")
    i5 = ImageName("debian", "jessie")
    i6 = ImageName("arch")

    assert c1.should_run(i1)
    assert c1.should_run(i2)
    assert not c1.should_run(i3)
    assert c1.should_run(i4)
    assert not c1.should_run(i5)
    assert not c1.should_run(i6)

    assert c2.should_run(i1)
    assert c2.should_run(i2)
    assert c2.should_run(i3)
    assert c2.should_run(i4)
    assert c2.should_run(i5)
    assert c2.should_run(i6)


def test_module_instantiation() -> None:
    """Test creating modules."""
    Module("example", [Component(RunRecipe())])
    Module("banana", [], "adds random bananas to your shell")
