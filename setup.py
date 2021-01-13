from setuptools import setup

setup(
    name = "sopp",
    version = "1.x",
    description = "A small, script for scraping website data using bs4.",
    py_modules = [],#Declare modules in this project
    package_dir = {"" : "src"},
    install_requires = [
        "beautifulsoup ~= 4.9.1",
    ]#External Dependencies
)