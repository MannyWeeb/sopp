from setuptools import setup

setup(
    name = "sopp",
    version = "1.x",
    description = "A small, script for scraping website data using bs4.",
    py_modules = [],
    package_dir = {"" : "src"},
    install_requires = [
        "beautifulsoup4 ~= 4.10.0",
        "requests ~= 2.25.1"
    ]#External Dependencies
)