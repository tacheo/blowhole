"""Test docker image classes."""

from os import path

import pytest
from pydantic import ValidationError

from blowhole.core.image import BuildRecipe, ImageName, RunRecipe

CURR_DIR = path.dirname(__file__)

YAML_EMPTY = path.join(CURR_DIR, "files", "empty.yaml")

IMAGENAME_FULL = path.join(CURR_DIR, "files", "imagename_full.yaml")
IMAGENAME_PARTIAL = path.join(CURR_DIR, "files", "imagename_partial.yaml")
IMAGENAME_INVALID = path.join(CURR_DIR, "files", "imagename_invalid.yaml")


def test_imagename_instantiation() -> None:
    """Test creating an ImageName."""
    ImageName("ghoti")
    ImageName("bolognese", "sauce")


def test_imagename_from_str_no_tag() -> None:
    """Test creating an ImageName from an untagged string."""
    image = ImageName.from_str("banana")

    assert image == ImageName("banana")


def test_imagename_from_str_with_tag() -> None:
    """Test creating an ImageName from a tagged string."""
    image = ImageName.from_str("bakery/bread:worryingly_moist")

    assert image == ImageName("bakery/bread", "worryingly_moist")


def test_imagename_from_bad_str() -> None:
    """Test creating an ImageName from a multi-tagged string."""
    with pytest.raises(ValueError):
        ImageName.from_str("a/b:c:d")


def test_imagename_eq() -> None:
    """Test ImageName equality."""
    i1 = ImageName("abc", "def")
    i2 = ImageName("abc", "def")
    i3 = ImageName("abc")
    i4 = ImageName("asd", "def")
    i5 = ["humpty", "dumpty", "had", "a", "great", "fall"]

    assert i1 == i2 and i2 == i1
    assert i1 != i3 and i3 != i1
    assert i1 != i4 and i4 != i1
    assert i1 != i5 and i5 != i1


def test_imagename_str() -> None:
    """Test string representations of image names."""
    i1 = ImageName("CHEESE")
    i2 = ImageName("a/b", "C")

    assert str(i1) == "CHEESE"
    assert str(i2) == "a/b:C"


def test_imagename_repr() -> None:
    """Test evaluable string representations of ImageName."""
    i1 = ImageName("a")
    i2 = ImageName("one", "two")
    i3 = ImageName("%^£\"'__3", "&**((£)_!:£~!!!")

    assert eval(repr(i1)) == i1
    assert eval(repr(i2)) == i2
    assert eval(repr(i3)) == i3


def test_imagename_comparisons() -> None:
    """Test comparing image names."""
    fish1 = ImageName("fish")
    fish2 = ImageName("fish", "3.6")

    assert fish1.is_compatible(fish2)
    assert fish2.is_compatible(fish2)
    assert not fish2.is_compatible(fish1)

    frog1 = ImageName("Frog", "twenty-seven")
    frog2 = ImageName("frog", "twenty-seven")

    assert not frog1.is_compatible(frog2)
    assert not frog2.is_compatible(frog1)


def test_imagename_load_from_empty() -> None:
    """Test loading empty file as ImageName."""
    with pytest.raises(TypeError):
        with open(YAML_EMPTY) as fp:
            ImageName.load_from_file(fp)


def test_imagename_load_full() -> None:
    """Test loading a full ImageName."""
    with open(IMAGENAME_FULL) as fp:
        assert ImageName.load_from_file(fp) == ImageName("banana", "13.76")


def test_imagename_load_partial() -> None:
    """Test loading a partial ImageName."""
    with open(IMAGENAME_PARTIAL) as fp:
        assert ImageName.load_from_file(fp) == ImageName("eee")


def test_imagename_load_invalid() -> None:
    """Test loading an invalid ImageName."""
    with pytest.raises(ValidationError):
        with open(IMAGENAME_INVALID) as fp:
            ImageName.load_from_file(fp)


BUILDRECIPE_VALID = path.join(CURR_DIR, "files", "buildrecipe_valid.yaml")
BUILDRECIPE_INVALID = path.join(CURR_DIR, "files", "buildrecipe_invalid.yaml")


def test_buildrecipe() -> None:
    """Create some build recipes."""
    BuildRecipe(["FROM ubuntu", "RUN rm -rf /", "EXPOSE 8080"])
    BuildRecipe([])


def test_buildrecipe_eq() -> None:
    """Test equality of build recipes."""
    b1 = BuildRecipe(["a", "b"])
    b2 = BuildRecipe(["a", "b"])
    b3 = BuildRecipe(["a"])
    b4 = BuildRecipe(["a", "q"])

    assert b1 == b2
    assert b2 == b1
    assert b1 != b3 and b3 != b1
    assert b1 != b4 and b4 != b1

    assert BuildRecipe([]) != "I did not hit her, I did not! Oh, hi Mark."


def test_buildrecipe_str() -> None:
    """Test human-readable string representation of BuildRecipe."""
    b1 = BuildRecipe([])
    b2 = BuildRecipe(["FROM java", "RUN cd ."])

    assert str(b1) == "BuildRecipe [\n]"
    assert str(b2) == (
        "BuildRecipe [\n"
        "\tFROM java\n"
        "\tRUN cd .\n"
        "]"
    )


def test_buildrecipe_build_str() -> None:
    """Test Dockerfile strings from BuildRecipe."""
    b1 = BuildRecipe([])
    b2 = BuildRecipe(["FROM example:17", "RUN setup-1", "EXPOSE 8080"])

    assert b1.build_str == ""
    assert b2.build_str == (
        "FROM example:17\n"
        "RUN setup-1\n"
        "EXPOSE 8080\n"
    )


def test_buildrecipe_repr() -> None:
    """Test evaluable string representation of BuildRecipe."""
    b1 = BuildRecipe([])
    b2 = BuildRecipe(
        ["dfafuho&*(*&^%", "8$&__*!", "@~@}{?>?"],
    )

    assert eval(repr(b1)) == b1
    assert eval(repr(b2)) == b2


def test_buildrecipe_add() -> None:
    """Test adding build recipes."""
    b1 = BuildRecipe()
    b2 = BuildRecipe(["1", "2", "3"])
    b3 = BuildRecipe()
    b4 = BuildRecipe(["4", "5"])
    b5 = BuildRecipe(["1", "2", "3", "4", "5"])

    assert b1 + b2 + b3 + b4 == b5

    b2 += b1
    b2 += b4
    b2 += b3

    assert b2 == b5


def test_buildrecipe_load_valid() -> None:
    """Test loading a valid BuildRecipe from file."""
    with open(BUILDRECIPE_VALID) as fp:
        assert BuildRecipe.load_from_file(fp) == BuildRecipe(commands=[
            "FROM test",
            "RUN cd .",
        ])


def test_buildrecipe_load_invalid() -> None:
    """Test loading an invalid BuildRecipe."""
    with pytest.raises(ValidationError):
        with open(BUILDRECIPE_INVALID) as fp:
            BuildRecipe.load_from_file(fp)


def test_buildrecipe_load_empty() -> None:
    """Test loading empty yaml as a BuildRecipe."""
    with open(YAML_EMPTY) as fp:
        assert BuildRecipe.load_from_file(fp) == BuildRecipe()


RUNRECIPE_VALID = path.join(CURR_DIR, "files", "runrecipe_valid.yaml")
RUNRECIPE_INVALID = path.join(CURR_DIR, "files", "runrecipe_invalid.yaml")


def test_runrecipe_instantiation() -> None:
    """Create some run recipes."""
    RunRecipe()
    RunRecipe(
        script=["ping 127.0.0.1 -n 1"],
        ports=[(8080, 3030), (1, 2)],
        sockets=[("/var/sock/example", "/var/sock/otherexample")],
        volumes=[("/beans", "/fries"), ("/toast", "/bread")],
    )


def test_runrecipe_eq() -> None:
    """Test equality of RunRecipes."""
    r1 = RunRecipe()
    r2 = RunRecipe(
        script=["ls"],
        ports=[(123, 456), (2, 3)],
        sockets=[("/var/yargh", "/var/aaargh")],
        volumes=[("/fish", "/fingers")],
    )
    r3 = RunRecipe(
        script=["ls"],
        ports=[(123, 456), (2, 3)],
        sockets=[("/var/yargh", "/var/aaargh")],
        volumes=[("/fish", "/fingers")],
    )
    r4 = RunRecipe(
        script=["ls -l"],
        ports=[(123, 456), (2, 3)],
        sockets=[("/var/yargh", "/var/aaargh")],
        volumes=[("/fish", "/fingers")],
    )

    assert r1 == r1
    assert r2 == r3 and r3 == r2
    assert r1 != r2 and r2 != r1
    assert r2 != r4 and r4 != r2

    assert RunRecipe() != 42


def test_runrecipe_str() -> None:
    """Test string representations of RunRecipe."""
    r = RunRecipe(
        script=["a"],
        ports=[(1, 2)],
        sockets=[("abc", "def")],
        volumes=[("ping", "pong")],
    )

    assert str(r) == (
        "RunRecipe ("
        f"\n\tscript={['a']},"
        f"\n\tports={[(1, 2)]},"
        f"\n\tsockets={[('abc', 'def')]},"
        f"\n\tvolumes={[('ping', 'pong')]},"
        "\n)"
    )

    assert eval(repr(r)) == r


def test_runrecipe_load_valid() -> None:
    """Test loading a valid run recipe from file."""
    with open(RUNRECIPE_VALID) as fp:
        assert RunRecipe.load_from_file(fp) == RunRecipe(
            script=["ping example.com", "git init"],
            ports=[(3, 2), (7, 204)],
            sockets=[("/var/opt/example", "/var/opt/otherthing")],
        )


def test_runrecipe_load_invalid() -> None:
    """Test loading an invalid run recipe from a file."""
    with pytest.raises(ValidationError):
        with open(RUNRECIPE_INVALID) as fp:
            RunRecipe.load_from_file(fp)


def test_runrecipe_load_empty() -> None:
    """Test loading empty yaml as a run recipe."""
    with open(YAML_EMPTY) as fp:
        assert RunRecipe.load_from_file(fp) == RunRecipe()
