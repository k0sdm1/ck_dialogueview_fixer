import argparse
import os
from tkinter import filedialog
from xml.etree import ElementTree as et


PATH_TO_TOOLTIP = 'Nodes/Node/ToolTip'
COUNT = 2

new_id = '07'


def check_is_hexadecimal(value: str):
    try:
        int(value, 16)
    except ValueError:
        print(f'{value} is not hexadecimal!')
        exit()


def absoluteFilePaths(directory):
    """Yields next dialogue view tuple (abs path,
    filename) in specified directory.
    """
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.xml':
                yield os.path.abspath(os.path.join(dirpath)), filename


def fix_dialogue_view(view_tuple: tuple, new_id: str):
    tree = et.parse(os.path.join(*view_tuple))
    all_tooltips = tree.findall(PATH_TO_TOOLTIP)
    for tooltip in all_tooltips:
        tooltip.text = tooltip.text.replace(
            tooltip.text[:COUNT], new_id, COUNT)
    tree.write(os.path.join(view_tuple[0], new_id + view_tuple[1][2:]))


def agrgument_parser():
    parser = argparse.ArgumentParser(description='CK dialogue view fixer')
    parser.add_argument('newid', help='New id (masters count) in HEX')
    args = parser.parse_args()
    check_is_hexadecimal(args.newid)
    global new_id
    new_id = args.newid


def main():
    path = filedialog.askdirectory()
    for file in absoluteFilePaths(path):
        fix_dialogue_view(file, new_id)


if __name__ == '__main__':
    agrgument_parser()
    main()
