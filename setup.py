import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuligetsheet",
    version="0.0.1",
    author="Moh Fahrul Hafidh",
    author_email="admin@kulitekno.com",
    description="A python package for Grab Google Sheet data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/H4rfu1/kuligetsheet",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ),
)