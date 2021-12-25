# -*- coding: utf-8 -*-
from setuptools import _install_setup_requires, setup

__author__ = "eseunghwan"
__email__ = "shlee0920@naver.com"
__version__ = "2021.12.25"

with open("requirements.txt", "r", encoding = "utf-8") as reqr:
    requires = reqr.read().split("\n")

with open("README.md", encoding = "utf-8") as rfr:
    readme = rfr.read()

with open("HISTORY.md", encoding = "utf-8") as hr:
    history = hr.read()


setup(
    # base informations
    author = __author__,
    author_email = __email__,
    version = __version__,
    url = "https://github.com/eseunghwan/tkcefview",
    # pip specfied informations
    python_requires = "<3.8",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    name = "tkcefview",
    keywords = [ "webview", "cef", "tkinter" ],
    description = "pywebview inspired tkinter framed cefpython3",
    long_description = readme,
    long_description_content_type = "text/markdown",
    license = "MIT license",
    # package data informations
    include_package_data = False,
    install_requires = requires,
    setup_requires = requires,
    packages = [ "tkcefview", "tkcefview/assets" ],
    package_data = {
        "": [
            "**/*.*",
            "**/**/*.*"
        ]
    },
    zip_safe = False
)