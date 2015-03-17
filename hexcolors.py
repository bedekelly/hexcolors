#!/usr/bin/env python3
import subprocess
import readline
import sys  # so heavy, but apparently just putting "unicode" makes people cry

# u+2588 is the full unicode block; 25A0 is a smaller square.
uni_square = bytes('\\u2588', 'ascii').decode('unicode-escape')

# Redefine a terminal color to use in this script.
begin_str = '\033]4;18;rgb:'

# Go out to shell for an accurate terminal width.
enc = sys.stdout.encoding
cols = int(subprocess.check_output(["tput", "cols"]).decode(enc))
lines = int(subprocess.check_output(["tput", "lines"]).decode(enc))
lines -= 1  # Make room for the input box.

# Print out the square, and reset the colour afterwards.
end_str = "\a\033[38;5;18m{}\033[m".format(uni_square*cols)

while True:
    try:
        hexcode = input("Hex code (e.g. FFFFFF): ")
    except (KeyboardInterrupt, EOFError):
        break
    subprocess.call("clear")
    color_str = "{}/{}/{}".format(hexcode[0:2], hexcode[2:4], hexcode[4:])
    printf_string = "{}{}{}".format(begin_str, color_str, end_str)
    for _ in range(lines):
        # Using system printf for correct escape-sequence support.
        subprocess.call(["printf", "{}\n".format(printf_string)])
