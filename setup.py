import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "statiq",
    version = "0.1.0",
    author = "Rastko",
    author_email = "rastko.vukasinovic@gmail.com",
    description = ("Static content generator and publisher"),
    license = "MIT",
    keywords = "static web page content generator",
    url = "",
    packages=['', ''],
    long_description=read('readme.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)