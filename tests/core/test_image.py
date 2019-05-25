"""Test docker image classes."""

import pytest

from blowhole.core.image import ImageName


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


def test_imagename_comparisons() -> None:
    """Test comparing image names."""
    fish1 = ImageName("fish")
    fish2 = ImageName("fish", "3.6")

    assert fish1 > fish2
    assert fish1 >= fish2
    assert not fish1 <= fish2
    assert not fish1 < fish2

    frog1 = ImageName("Frog", "twenty-seven")
    frog2 = ImageName("frog", "twenty-seven")
    assert not frog1 > frog2
    assert not frog1 >= frog2
    assert not frog1 == frog2
