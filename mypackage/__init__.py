"""A simple test package for uploading to private PyPI."""

try:
    from mypackage._version import version as __version__
except ImportError:
    __version__ = "unknown"