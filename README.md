

# eRCaGuy_PyColors

For text formatting and colorization in the terminal.

A Python module to add ANSI color and format codes to strings for terminal output.


# Installation

Install from PyPI (once published):
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
python3 -m venv ~/venvs/eRCaGuy_PyColors
source ~/venvs/eRCaGuy_PyColors/bin/activate
# Now install as above
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

See: https://packaging.python.org/en/latest/tutorials/packaging-projects/

For maintainers, to publish a new version to PyPI:

1. Install or upgrade `twine`: 
    ```bash
    python3 -m pip install --upgrade twine build
    ```
1. Update the version number in `pyproject.toml`
1. Build the distribution packages:
    ```bash
    python3 -m build
    ```
1. Test an upload to TestPyPI first (recommended):
    ```bash
    python3 -m twine upload --repository testpypi dist/*
    ```
1. Test an installation in a virtual environment from TestPyPI:
    ```bash
    python3 -m venv ~/venvs/test_eRCaGuy_PyColors
    source ~/venvs/test_eRCaGuy_PyColors/bin/activate
    pip install --index-url https://test.pypi.org/simple/ --no-deps eRCaGuy_PyColors
    ```
    Test that it works as expected.
1. Upload to PyPI using twine:
    ```bash
    python3 -m twine upload dist/*
    ```
1. Test an installation in a virtual environment from PyPI:
    ```bash
    python3 -m venv ~/venvs/eRCaGuy_PyColors
    source ~/venvs/eRCaGuy_PyColors/bin/activate
    pip install eRCaGuy_PyColors
    ```
    Test that it works as expected.


# References

1. Borrowed from my file here: https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/python/pandas_dataframe_iteration_vs_vectorization_vs_list_comprehension_speed_tests.py
1. https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/python/ansi_colors.py
1. https://github.com/ElectricRCAircraftGuy/eRCaGuy_PathShortener/blob/main/ansi_colors.py <==
1. My Bash ANSI format library here: https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/bash/ansi_text_format_lib.sh
1. https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit

