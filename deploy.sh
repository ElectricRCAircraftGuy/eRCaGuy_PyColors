#!/usr/bin/env bash

# Deploy eRCaGuy_PyColors to PyPI

# build
time python3 -m build

# upload
python3 -m twine upload dist/*
