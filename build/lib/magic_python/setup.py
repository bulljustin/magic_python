import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magic-python", # Replace with your own username
    version="0.0.1",
    author="Justin Frazier",
    author_email="justin@jmfrazier.com",
    description="Adding constant that can be used in place of magic string and numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bulljustin/magic_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
