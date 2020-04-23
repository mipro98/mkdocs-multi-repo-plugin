#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name="edit_url",
    version='0.1',
    install_requires=['mkdocs>=1.0.4'],
    packages=["edit_url"],
    entry_points={
        'mkdocs.plugins': [
            'edit_url = edit_url.plugin:EditUrlPlugin',
        ]
    }
)
