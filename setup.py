#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = [
    "black>=19.10b0",
    "codecov>=2.1.4",
    "flake8>=3.8.3",
    "flake8-debugger>=3.2.1",
    "parameterized>=0.8.0",
    "pytest>=5.4.3",
    "pytest-cov>=2.9.0",
    "pytest-raises>=0.11",
]

dev_requirements = [
    *test_requirements,
    "bumpversion>=0.6.0",
    "coverage>=5.1",
    "ipython>=7.15.0",
    "m2r>=0.2.1",
    "pytest-runner>=5.2",
    "Sphinx>=2.0.0b1,<3",
    "sphinx_rtd_theme>=0.4.3",
    "tox>=3.15.2",
    "twine>=3.1.1",
    "wheel>=0.34.2",
]

extra_requirements = {
    "test": test_requirements,
    "dev": dev_requirements,
    "all": [
        *requirements,
        *dev_requirements,
    ]
}

setup(
    author="Kevin Alex Zhang",
    author_email="kevz@mit.edu",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Generate unique strings from regular expressions.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="intxeger",
    name="intxeger",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    entry_points={
        'console_scripts': [
            'intxeger=intxeger.__main__:main',
        ],
    },
    python_requires=">=3.6",
    test_suite="intxeger/tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/k15z/intxeger",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="0.1.1",
    zip_safe=False,
)
