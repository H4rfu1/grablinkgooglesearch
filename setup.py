import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grablinkgooglesearch",
    version="0.0.5",
    author="Moh Fahrul Hafidh",
    author_email="admin@kulitekno.com",
    description="A python package for Grab Link Google Search and export it to a file csv or txt.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/H4rfu1/grablinkgooglesearch",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ),
)