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

from eRCaGuy_PyColors.ansi_colors import (
    # ANSI codes and color constants
    ANSI_START,
    ANSI_FG_GRE,
    ANSI_FG_BLU,
    ANSI_FG_BR_BLU,
    ANSI_FG_RED,
    ANSI_FG_BR_RED,
    ANSI_FG_BR_YEL,
    ANSI_END,
    ANSI_OFF,
    F,
    END,
    FGN,
    FGR,
    FBL,
    FBB,
    FRE,
    FBR,
    FBY,
    # Print functions
    print_red,
    print_yellow,
    print_green,
    print_blue,
)

__version__ = "0.1.1"
__author__ = "Gabriel Staples"
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
