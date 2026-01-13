#!/usr/bin/env bash

# Deploy eRCaGuy_PyColors to PyPI

echo "Deploying eRCaGuy_PyColors to PyPI..."
echo "- NB: no new changes will be deployed apparently if the version number in"
echo "  eRCaGuy_PyColors/__init__.py has not been changed since the last deploy."
echo ""

# Prerequisites
pip install --upgrade pip
python3 -m pip install --upgrade twine build

# build
time python3 -m build

# upload
python3 -m twine upload dist/*

echo ""
echo "See package at https://pypi.org/project/eRCaGuy-PyColors/"

