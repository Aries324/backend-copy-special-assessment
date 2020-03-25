#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import re
import os
import shutil
import subprocess
import argparse


"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
__author__ = "Tiffany McLean with the help of demo"

"""
create a helper function
"""


def get_special_paths(dir):
    """Manipulate file path"""
    special_paths = []
    files = os.listdir(dir)
    for file in files:
        if re.search(r'__\w+__', file):
            special_paths.append(file)
    return special_paths


def copy_to(path, files):
    """This will copy special files to a directory"""
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('Path exists')

    for file in files:
        shutil.copy(file, path)


def zip_to(paths, zippath):
    """ Creates zipfiles from specialfiles"""
    paths = list(paths)
    command = 'zip -j {} {}'.format(zippath, ' '.join(paths))
    print(command)
    # runs the command in the terminal as if you just typed it into the terminal
    os.system(command)


def zip_to_two(paths, zippath):
    command = ['zip', '-j', zippath]
    command.extend(paths)
    print('Command I am going to do: {}'.format(' '.join(command)))
    subprocess.check_output(command)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='src dir to look for local files')
    args = parser.parse_args()

    all_paths = get_special_paths(args.fromdir)

    if args.todir:
        copy_to(args.todir, all_paths)

    if args.tozip:
        zip_to_two(all_paths, args.tozip)

    if not args.todir and not args.tozip:
        print('\n'.join(all_paths))


if __name__ == "__main__":
    main()
