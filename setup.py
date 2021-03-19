import os

from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), "r") as f:
        return f.read()


setup(
    name="unmain",
    version="1.0.0",
    py_modules=["unmain"],
    url="https://github.com/tmr232/unmain",
    license="MIT",
    author="Tamir Bahar",
    author_email="",
    package_dir={"": "src"},
    description="The end to __name__ == __main__",
    long_description=(read("README.rst")),
)
