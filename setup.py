#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name="mkdocs-multi-repo-plugin",
    version='0.1',
    install_requires=['mkdocs>=1.0.4'],
    packages=["multi_repo"],
    entry_points={
        'mkdocs.plugins': [
            'multi_repo = multi_repo.plugin:MultiRepoPlugin',
        ]
    }
)
