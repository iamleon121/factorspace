#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Leon
# Mail: iamleon@yeah.net
# Created Time:  2019-4-26 15:00:00
#############################################


from setuptools import setup, find_packages

setup(
    name = "factorspace",
    version = "0.3.0",
    keywords = ("factor", "factorspace","space"),
    description = "factor space analysis tool",
    long_description = "factor space analysis tool",
    license = "MIT Licence",

    url = "https://github.com/iamleon121/factorspace",
    author = "Leon Tian",
    author_email = "iamleon@yeah.net",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
