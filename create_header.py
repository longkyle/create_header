#!/usr/bin/env python

"""
Automates header creation for python scripts/files
"""

__author__ = "Kyle Long"
__email__ = "long.kyle@gmail.com"
__date__ = "08/26/2019"
__copyright__ = "Copyright 2019, Kyle Long"
__python_version__ = "3.7.4"


import os
import sys
from time import strftime
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', action="store", type=str)
    args = parser.parse_args()
    filename = args.filename

    if not filename.endswith('.py'):
        print(f'"{filename}" does not end with ".py"')
        return

    # Check to see if the file exists to not overwrite it.
    if os.path.exists(filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        try:
            if lines[0].startswith('#!/usr/bin/env python'):
                print(f'"{filename}" already has a header')

                return

        # Must be an empty file, which is fine.
        except IndexError:
            pass

    else:

        # Convert all letters to lower case.
        filename = filename.lower()

        # Remove spaces from the title.
        filename = filename.replace(' ', '_')

        # Create new file
        f = open(filename, 'w')
        lines = []
        f.close()

    # Get docstring for file/script
    descrpt = input(f'Please enter a docstring for {filename}: ')

    # Author info
    name = 'Kyle Long'
    email_address = 'long.kyle@gmail.com'

    # Set the date automatically.
    date = strftime("%m/%d/%Y")
    year = strftime("%Y")

    # Determine Python version
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    py_ver = f'{major}.{minor}.{micro}'

    divider = "#" + ' -' * 15 + "PEP8 length guide" + '- ' * 15 + '-'

    # Create new lines to prepend to the original file
    new_lines = \
        '#!/usr/bin/env python\n' \
        '\n' \
        '"""\n' \
        f'{descrpt}\n' \
        '"""\n' \
        '\n' \
        f'__author__ = "{name}"\n' \
        f'__email__ = "{email_address}"\n' \
        f'__date__ = "{date}"\n' \
        f'__copyright__ = "Copyright {year}, {name}"\n' \
        f'__python_version__ = "{py_ver}"\n' \
        '\n' \
        f'{divider}' \
        '\n' \
        '\n'

    lines.insert(0, new_lines)

    # Open file, write lines, and close
    new_f = open(filename, 'w')
    new_f.writelines(lines)
    new_f.close()

    os.system(f'subl {filename}')

    print(len(divider))


if __name__ == '__main__':
    main()
