#!/usr/bin/env python3
import subprocess
import readline
import sys  # so heavy, but apparently just putting "unicode" makes people cry

# u+2588 is the full unicode block; 25A0 is a smaller square.
uni_square = bytes('\\u2588', 'ascii').decode('unicode-escape')

# Redefine a terminal color to use in this script.
begin_str = '\033]4;18;rgb:'

# Get the terminal width
enc = sys.stdout.encoding
cols = int(subprocess.check_output(["tput", "cols"]).decode(enc))

# Print out the square a good few times. Also fix the color back to normal.
end_str = "\a\033[38;5;18m{}\033[m".format(uni_square*cols)


while True:
    try:
        hexcode = input("Hex code (e.g. FFFFFF): ")
    except (KeyboardInterrupt, EOFError):
        print(); quit()  # whatever
    subprocess.call("clear")
    color_str = "{}/{}/{}".format(hexcode[0:2], hexcode[2:4], hexcode[4:])
    printf_string = begin_str + color_str + end_str  # String concatenation, and what
    # Using printf, since the print() function doesn't like ANSI escapes.
    subprocess.call(["printf", "{}\n".format(printf_string)])
