#!/usr/bin/env python3

"""
A Python module to add ANSI color and format codes to strings for terminal output.

By Gabriel Staples
https://github.com/ElectricRCAircraftGuy/eRCaGuy_PyColors

"""


ANSI_START = "\033["    # start of an ANSI formatting sequence

ANSI_FG_GRE = ";32"     # foreground color green
ANSI_FG_BLU = ";34"     # foreground color blue
ANSI_FG_BR_BLU = ";94"  # foreground color bright blue
ANSI_FG_RED = ";31"    # foreground color red
ANSI_FG_BR_RED = ";91" # foreground color bright red
ANSI_FG_BR_YEL = ";93" # foreground color bright yellow

ANSI_END = "m"          # end of an ANSI formatting sequence

ANSI_OFF = f"{ANSI_START}{ANSI_END}"
F = ANSI_OFF    # alias
END = ANSI_OFF  # alias

FGN = ANSI_OFF                                   # Foreground None: normal, uncolored text
FGR = f"{ANSI_START}{ANSI_FG_GRE}{ANSI_END}"     # green text
FBL = f"{ANSI_START}{ANSI_FG_BLU}{ANSI_END}"     # blue text
FBB = f"{ANSI_START}{ANSI_FG_BR_BLU}{ANSI_END}"  # bright blue text
FRE = f"{ANSI_START}{ANSI_FG_RED}{ANSI_END}"     # red text
FBR = f"{ANSI_START}{ANSI_FG_BR_RED}{ANSI_END}"  # bright red text
FBY = f"{ANSI_START}{ANSI_FG_BR_YEL}{ANSI_END}"  # bright yellow text


def print_red(*args, **kwargs):
    """
    Print the arguments in bright red text.
    - Accepts all the same arguments as the built-in `print()` function.
    """

    # NOT QUITE RIGHT
    # print(f"{colors.FRE}", *args, f"{colors.END}", **kwargs)

    # ALSO NOT QUITE RIGHT
    # print(f"{colors.FRE}" + args[0], args[1:], f"{colors.END}", **kwargs)

    # Works!
    # Concatenate the red color code with each argument
    colored_args = [f"{FBR}{arg}{END}" for arg in args]
    # Print the colored arguments
    print(*colored_args, **kwargs)


def print_yellow(*args, **kwargs):
    """
    Print the arguments in bright yellow text.
    - Accepts all the same arguments as the built-in `print()` function.
    """
    colored_args = [f"{FBY}{arg}{END}" for arg in args]
    print(*colored_args, **kwargs)


def print_green(*args, **kwargs):
    """
    Print the arguments in green text.
    - Accepts all the same arguments as the built-in `print()` function.
    """
    colored_args = [f"{FGR}{arg}{END}" for arg in args]
    print(*colored_args, **kwargs)


def print_blue(*args, **kwargs):
    """
    Print the arguments in bright blue text.
    - Accepts all the same arguments as the built-in `print()` function.
    """
    colored_args = [f"{FBB}{arg}{END}" for arg in args]
    print(*colored_args, **kwargs)


def run_tests():
    # Test the colors

    print(f"{FGR}This text is green.{END}")
    print(f"{FBB}This text is bright blue.{END}")

    print_red("This text is bright red.")
    print_red("This text", "is bright red.")
    print_red("This text", "is", "bright", "red.")

    print_red("This text", "is", end=" ")  # end with a space instead of a newline
    print_red("bright", "red.")

    print_red("This text", "is")
    print_red("  bright", "red.")

    print_yellow("This text is bright yellow.")
    print(f"{FGN}This text is not colored.{END}")
    print_yellow("This text is bright yellow again.")

    print_green("This text is green.")


# Define what gets exported with `from eRCaGuy_PyColors import *`, or `from .ansi_colors import *`
#
# Notes to self when using the `import *` ("import all") type syntax:
# - If this `ansi_colors.__all__` list exists, only items from this list are imported.
# - If this `ansi_colors.__all__` list does NOT exist, all items in this module NOT starting with an
#   underscore are automatically imported.
__all__ = [
    # ANSI codes and color constants
    "ANSI_START",
    "ANSI_FG_GRE",
    "ANSI_FG_BLU",
    "ANSI_FG_BR_BLU",
    "ANSI_FG_RED",
    "ANSI_FG_BR_RED",
    "ANSI_FG_BR_YEL",
    "ANSI_END",
    "ANSI_OFF",
    "F",
    "END",

    "FGN",
    "FGR",
    "FBL",
    "FBB",
    "FRE",
    "FBR",
    "FBY",
    # Print functions
    "print_red",
    "print_yellow",
    "print_green",
    "print_blue",
]


if __name__ == "__main__":
    run_tests()
