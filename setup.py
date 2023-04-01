from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="uule_grabber",
    packages=["uule_grabber"],
    version="0.1.9",
    description="Generates UULE codes for Google Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kemal Ogun Isik",
    author_email="ogunisik@gmail.com",
    url="https://github.com/ogun/uule_grabber",
    download_url="https://github.com/ogun/uule_grabber/archive/v0.1.9.tar.gz",
    classifiers=[],
)
