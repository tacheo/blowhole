"""Test docker image classes."""

import pytest

from blowhole.core.image import BuildRecipe, ImageName, RunRecipe


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

    assert repr(i1) == "ImageName('a')"
    assert eval(repr(i1)) == i1
    assert repr(i2) == "ImageName('one', 'two')"
    assert eval(repr(i2)) == i2
    assert repr(i3) == "ImageName('%^£\"\\'__3', '&**((£)_!:£~!!!')"
    assert eval(repr(i3)) == i3


def test_imagename_comparisons() -> None:
    """Test comparing image names."""
    fish1 = ImageName("fish")
    fish2 = ImageName("fish", "3.6")

    assert fish1.is_compatible(fish2)
    assert not fish2.is_compatible(fish1)

    frog1 = ImageName("Frog", "twenty-seven")
    frog2 = ImageName("frog", "twenty-seven")

    assert not frog1.is_compatible(frog2)
    assert not frog2.is_compatible(frog1)


def test_imagename_equality_with_garbage() -> None:
    """Test comparing an ImageName to random garbage."""
    with pytest.raises(NotImplementedError):
        ImageName("e") == ["humpty", "dumpty", "had", "a", "great", "fall"]


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


def test_buildrecipy_eq_garbage() -> None:
    """Test equality of build recipe with random garbage."""
    with pytest.raises(NotImplementedError):
        BuildRecipe([]) == "I did not hit her, I did not! Oh, hi Mark."


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


def test_buildrecipe_repr() -> None:
    """Test evaluable string representation of BuildRecipe."""
    b1 = BuildRecipe([])
    b2 = BuildRecipe(
        ["dfafuho&*(*&^%", "8$&__*!", "@~@}{?>?"],
    )

    assert eval(repr(b1)) == b1
    assert eval(repr(b2)) == b2


def test_runrecipe_instantiation() -> None:
    """Create some run recipes."""
    RunRecipe()
    RunRecipe(
        script=["ping 127.0.0.1 -n 1"],
        ports=[(8080, 3030), (1, 2)],
        sockets=[("/var/sock/example", "/var/sock/otherexample")],
        volumes=[("/beans", "/fries"), ("/toast", "/bread")],
    )
