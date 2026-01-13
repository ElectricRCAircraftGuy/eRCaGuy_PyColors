"""
eRCaGuy_PyColors - A Python module for ANSI color and format codes in terminal output.

By Gabriel Staples
https://github.com/ElectricRCAircraftGuy/eRCaGuy_PyColors

Example usage:
    import eRCaGuy_PyColors as colors

    print(f"{colors.FGR}This text is green.{colors.END}")
    print(f"{colors.FBB}This text is bright blue.{colors.END}")

    colors.print_green("This text is green.")
    colors.print_blue("This text is bright blue.")
    colors.print_red("This text is bright red.")
    colors.print_yellow("This text is bright yellow.")
"""

# NB: use relative imports here to avoid import issues when importing this package directly
# as a submodule from a higher-level repo.
# Notes to self when using the `import *` ("import all") type syntax:
# - If the `ansi_colors.__all__` list exists, only items from that list are imported.
# - If the `ansi_colors.__all__` list does NOT exist, all items in that module NOT starting with an
#   underscore are automatically imported.
from .ansi_colors import *

# NB: This version number **must** be incremented, and the changes fully committed in git, to
# trigger a new release on PyPI when you run `./deploy.sh`.
__version__ = "0.1.5"
__author__ = "Gabriel Staples"
