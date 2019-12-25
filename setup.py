# Commands to run
# Build deployment package
# python setup.py sdist bdist_wheel
# deploy to test.pypi.org
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose
# Test API Token (when pasting into powershell, use right-click instead of ctrl + v
# pypi-AgENdGVzdC5weXBpLm9yZwIkNTBiOTZmYzQtNTcwZC00NDk2LTkwZGQtMjQ3ZDZjOWI0OGZhAAI8eyJwZXJtaXNzaW9ucyI6IHsicHJvamVjdHMiOiBbIm1hZ2ljcHl0aG9uIl19LCAidmVyc2lvbiI6IDF9AAAGIJ6zttCSnRyqpx3CpXK-qKPiguoPNoQF_91TbmU8EmR1
# deploy to pypi.org
# python -m twine upload --repository-url https://pypi.org/legacy/ dist/* --verbose
try:
  import setuptools
  from setuptools import setup
except ImportError:
  from distutils.core import setup
import time

with open("README.md", "r") as fh:
  long_description = fh.read()
  print(long_description)

major = 0
minor = 0
micro = 1
# TODO there ought to be a way to determine from the incoming args whether this
# is going to be a test deployment or not
useCurrent = True
#useCurrent = False
if(useCurrent):
  current = str(int(time.time()))[-5:]
  version = f"{major}.{minor}.{micro}.{current}"
  import os
  dir_path = os.path.dirname(os.path.realpath(__file__))+"\\dist\\"
  filelist = [f for f in os.listdir(dir_path)]
  for f in filelist:
      os.remove(os.path.join(dir_path, f))
else:
  version = f"{major}.{minor}.{micro}"

setuptools.setup(name="MagicPython",
    version=version,
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
