"""A simple greeting module."""


class Greet:
    """A simple class to perform a greeting."""

    def __init__(self, name: str):
        self.name = name

    def say_hello(self) -> str:
        """Returns a greeting message."""
        return f"Hello, {self.name}!"
