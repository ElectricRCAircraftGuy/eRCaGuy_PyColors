

# eRCaGuy_PyColors

For text formatting and colorization in the terminal.

A Python module to add ANSI color and format codes to strings for terminal output.


# References

1. Borrowed from my file here: https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/python/pandas_dataframe_iteration_vs_vectorization_vs_list_comprehension_speed_tests.py
1. https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/python/ansi_colors.py
1. https://github.com/ElectricRCAircraftGuy/eRCaGuy_PathShortener/blob/main/ansi_colors.py <==
1. My Bash ANSI format library here: https://github.com/ElectricRCAircraftGuy/eRCaGuy_hello_world/blob/master/bash/ansi_text_format_lib.sh
1. https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit


# Test and run this program

```bash
./ansi_colors.py
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


# Example usage in your Python program

```python
import eRCaGuy_PyColors.ansi_colors as colors

print(f"{colors.FGR}This text is green.{colors.END}")
print(f"{colors.FBB}This text is bright blue.{colors.END}")
print(f"{colors.FBR}This text is bright red.{colors.END}")

colors.print_green("This text is green.")
colors.print_blue("This text is bright blue.")
colors.print_red("This text is bright red.")
```
