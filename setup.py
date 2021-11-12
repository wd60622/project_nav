#!/usr/bin/env python

from setuptools import setup

setup(
    name="project-nav",
    version="0.0.1",
    author="William Dean",
    author_email="wdean@homepartners.com",
    description="Quickly navigate between project directories.",
    packages=["project_nav"],
    scripts=["scripts/nav"],
    package_data={"": ["*"]},
    install_requires=["typer", "rich", "pyyaml"],
    include_package_data=True,
)
