import subprocess
import sys

# 2B1B is the larger unicode square; 25A0 is smaller.
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
        print(); quit()
    subprocess.call("clear")
    color_str = "{}/{}/{}".format(hexcode[0:2], hexcode[2:4], hexcode[4:])
    printf_string = begin_str + color_str + end_str
    # Using printf, since the print() function doesn't like ANSI escapes.
    subprocess.call(["printf", "{}\n".format(printf_string)])