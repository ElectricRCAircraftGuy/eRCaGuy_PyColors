#!/usr/bin/env bash

# Deploy a new release of eRCaGuy_PyColors to PyPI, and auto-tag the release in git.
# Usage: `./deploy.sh`

echo "Deploying eRCaGuy_PyColors to PyPI..."
echo "- NB: no new changes will be deployed apparently if the version number in"
echo "  eRCaGuy_PyColors/__init__.py has not been changed since the last deploy."
echo ""

# Ensure `git status` is clean before a deploy
if [[ -n $(git status --porcelain) ]]; then
    echo "ERROR: git status is not clean! Please commit or stash your changes before deploying."
    echo "'git status' output:"
    echo ""
    git status
    exit 1
fi

# Ensure prerequisites are installed
pip install --upgrade pip
python3 -m pip install --upgrade twine build

# Clean the old build
rm -rf dist/ build/ *.egg-info

# build
time python3 -m build

# Upload. If it passes, tag the version in git and push the tag.
python3 -m twine upload dist/*
if [ $? -eq 0 ]; then
    # Get version from __init__.py
    VERSION=$(python3 -c "from eRCaGuy_PyColors import __version__; print(__version__)")

    echo ""
    echo "Upload successful! Tagging current commit as version v${VERSION} in git..."
    git tag -a "v${VERSION}" -m "Release v${VERSION}"
    git push origin "v${VERSION}"
    echo "Tagged and pushed v${VERSION}"
else
    echo ""
    echo "ERROR: Upload to PyPI failed. Not tagging in git. You probably need to increment the" \
         "version number in 'eRCaGuy_PyColors/__init__.py' to trigger a new upload."
    exit 1
fi

echo ""
echo "See package at https://pypi.org/project/eRCaGuy-PyColors/"

