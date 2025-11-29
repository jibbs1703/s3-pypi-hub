"""Unit tests for the Greet class in testpackage.greet module."""

import pytest

from testpackage.greet import Greet


@pytest.mark.unit
def test_say_hello():
    """Test the say_hello method of Greet class."""
    name = "Alice"
    greeter = Greet(name)
    assert greeter.say_hello() == f"Hello, {name}!"


@pytest.mark.unit
def test_empty_name():
    """Test the say_hello method of Greet class with an empty name."""
    name = ""
    greeter = Greet(name)
    assert greeter.say_hello() == "Hello, !"
