

# eRCaGuy_PyColors

For text formatting and colorization in the terminal.

A Python module to add ANSI color and format codes to strings for terminal output.


# Installation

Upgrade pip first (optional but recommended):
```bash
pip install --upgrade pip
# or (more explicit)
python3 -m pip install --upgrade pip
```

Install from PyPI: https://pypi.org/project/eRCaGuy-PyColors/:
```bash
pip install eRCaGuy_PyColors
```

Or install from source:
```bash
git clone https://github.com/ElectricRCAircraftGuy/eRCaGuy_PyColors.git
cd eRCaGuy_PyColors
pip install .
```

For development (editable install):
```bash
pip install -e .
```

To install into a virtual environment:
```bash
# Create and activate a virtual environment
cd path/to/repo/eRCaGuy_PyColors
rm -rf .venv1/          # remove old venv if it exists
python3 -m venv .venv1  # create a new virtual environment in dir `.venv1/`
. .venv1/bin/activate   # activate the virtual environment

# To see if you're in a virtual environment, run:
echo "$VIRTUAL_ENV"
# If in a virtual environment, this will print the path to the virtual environment.
# Otherwise, it will print nothing.

# Now that you are inside the virtual environment, install as above. Ex: 
# Option 1: install from PyPI:
pip install eRCaGuy_PyColors
# Option 2: install from source: 
# - Inside of the `eRCaGuy_PyColors` repo: 
pip install .

# Now test the install in a temp dir to ensure imports don't import from the source dir directly
# accidentally. ie: we want to test the package we just installed above, not the source code 
# package in this repo directly.
mkdir temp/
cd temp/
# test it
python3 -c 'import eRCaGuy_PyColors as c; c.print_blue("hey")'               # prints "hey" in blue
python3 -c 'import eRCaGuy_PyColors.ansi_colors as c2; c2.print_blue("hi")'  # prints "hi" in blue
# cd back up to the root of the main repo when done
cd ..

# deactivate the virtual environment when done testing
# - this is only a valid command when inside a virtual environment
deactivate
```


# Example usage in your Python program

```python
# Recommended import style
import eRCaGuy_PyColors as colors
# OR (older style): 
# import eRCaGuy_PyColors.ansi_colors as colors

print(f"{colors.FGR}This text is green.{colors.END}")
print(f"{colors.FBB}This text is bright blue.{colors.END}")
print(f"{colors.FBR}This text is bright red.{colors.END}")

colors.print_green("This text is green.")
colors.print_blue("This text is bright blue.")
colors.print_red("This text is bright red.")
colors.print_yellow("This text is bright yellow.")
```


# Test and run this program

Run the built-in tests:
```bash
python3 -m eRCaGuy_PyColors
```

Example run and output: 
```bash
eRCaGuy_PyColors$ ./ansi_colors.py 
This text is green.
This text is bright blue.
This text is bright red.
This text is bright red.
This text is bright red.
This text is bright red.
This text is
  bright red.
This text is bright yellow.
This text is not colored.
This text is bright yellow again.
This text is green.
```

Screenshot:
<p align="left" width="100%">
    <a href="https://github.com/user-attachments/assets/f65a9312-7d1b-4a68-8edc-352e591750b8">
        <img width="40%" src="https://github.com/user-attachments/assets/f65a9312-7d1b-4a68-8edc-352e591750b8"> 
    </a>
</p>


# Publishing to PyPI

See: 
1. https://packaging.python.org/en/latest/tutorials/packaging-projects/
1. https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
1. Looks really useful!: https://realpython.com/pypi-publish-python-package/ 

For maintainers, to publish a new version to PyPI:

#### Short version
```bash
./deploy.sh
```

#### Details
1. Install or upgrade `twine`: 
    ```bash
    python3 -m pip install --upgrade twine build
    ```
1. Update the version number in `eRCaGuy_PyColors/__init__.py`.  
    
    NB: no new changes will be deployed to PyPI if the version number in `eRCaGuy_PyColors/__init__.py` has not been changed since the last upload.
1. Clean the old build. 

    NB: Updating the version number above, _plus_ cleaning the old build like this, are _both_ required to ensure a successful new upload to PyPI.
    ```bash
    rm -rf dist/ build/ *.egg-info
    ```
1. Build the distribution packages according to the settings in `pyproject.toml`:
    ```bash
    time python3 -m build
    ```
1. (Recommended) upload to TestPyPI using `twine`: 

    Test an upload to TestPyPI first:
    1. Log into your TestPyPI account at https://test.pypi.org/. 
    1. Obtain an API token at https://test.pypi.org/manage/account/#api-tokens --> "Add API token" --> (Activate two-factor authentication, if not yet done, to enable token generation.) --> Set "Token name" to `Gabriel TestPyPI` (using your name); set "Scope" to `Entire account (all projects)` --> click "Create token". Follow the instructions there. ie: create a `~/.pypirc` file with the following contents:
        `~/.pypirc`:
        ```ini
        [testpypi]
        username = __token__
        password = <your TestPyPI API token here, without the angle brackets>

        [pypi]
        username = __token__
        password = <your PyPI API token here, without the angle brackets>
        ```
        Paste your TestPyPI API token into the `password` field under `[testpypi]`, and save the file. 
    1. Upload using `twine`:
        ```bash
        python3 -m twine upload --repository testpypi dist/*
        ```
1. Test an installation in a virtual environment from TestPyPI:
    ```bash
    rm -rf .venv2/
    python3 -m venv .venv2
    . .venv2/bin/activate
    pip install --index-url https://test.pypi.org/simple/ --no-deps eRCaGuy_PyColors
    ```
    Test that it works as expected.
1. Upload to PyPI using `twine`:
    1. Log into your PyPI account at https://pypi.org/.
    1. Obtain an API token at https://pypi.org/manage/account/#api-tokens --> "Add API token" --> (Activate two-factor authentication, if not yet done, to enable token generation.) --> Set "Token name" to `Gabriel PyPI` (using your name); set "Scope" to `Entire account (all projects)` --> click "Create token". Follow the instructions there. ie: update your `~/.pypirc` file by pasting in your token under the `[pypi]` section as shown above.
    1. Upload using `twine`:
        ```bash
        python3 -m twine upload dist/*
        ```
1. Test an installation in a virtual environment from PyPI:
    ```bash
    rm -rf .venv3/
    python3 -m venv .venv3
    . .venv3/bin/activate
    pip install eRCaGuy_PyColors
    ```
    Test that it works as expected.


# References

1. Borrowed from my file here: https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/python/pandas_dataframe_iteration_vs_vectorization_vs_list_comprehension_speed_tests.py
1. https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/python/ansi_colors.py
1. https://github.com/ElectricRCAircraftGuy/eRCaGuy_PathShortener/blob/main/ansi_colors.py <==
1. My Bash ANSI format library here: https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/bash/ansi_text_format_lib.sh
1. https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit

