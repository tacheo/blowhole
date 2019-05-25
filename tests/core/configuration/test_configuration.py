"""Tests for the base configuration class."""

import os

from typesystem import Integer

from blowhole.core.configuration import Configuration


class MockConfiguration(Configuration):
    """A mock configuration type for testing."""

    count = Integer()


def test_load_from_dict() -> None:
    """Test if we can load from a dict."""
    val = MockConfiguration.validate({
        'count': 4,
    })

    assert val is not None
    assert val.count == 4  # type: ignore


def test_load_from_file() -> None:
    """Test if we can load from a file."""
    with open(os.path.join(os.path.dirname(__file__), 'mockconfig.yml')) as fp:
        val = MockConfiguration.load_file(fp)
        assert val is not None
        assert val.count == 10
