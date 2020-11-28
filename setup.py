import os
from setuptools import setup, find_packages

setup(
    name = "ci_test",
    version = "0.0.1",
    author = "Emanuel Huber",
    author_email = "emanuel.tesv@gmail.com",
    description = ("An demonstration of Github Actions + pytest."),
    license = "BSD",
    keywords = "example tutorial",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    long_description="Imagine a long description",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
