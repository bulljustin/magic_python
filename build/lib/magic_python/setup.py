try:
  import setuptools
  from setuptools import setup
except ImportError:
  from distutils.core import setup
from datetime import datetime

with open("README.md", "r") as fh:
    long_description = fh.read()

current = time()

setuptools.setup(name="magic-python",
    version=f"0.0.1.{current}",
    author="Justin Frazier",
    author_email="justin@jmfrazier.com",
    description="Adding constants and functions that can be used in place of magic string, magic numbers, and abbreviated function names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bulljustin/magic_python",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",],
    python_requires='>=3.0',)
