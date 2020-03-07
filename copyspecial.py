#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import sys
import re
import os
import shutil
import subprocess
import argparse
from argparse import RawTextHelpFormatter

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
__author__ = "Sarah Gale"


def is_special_path(a_path):
    """
    a_path may be a file or a directory
    if path is not special, return False
    if path is special, return True
    """
    match = re.search(r'__\w+__', a_path)
    if match is None:
        is_special = False
    else:
        is_special = True
    return is_special


def get_special_paths(a_dir):
    """
    return a list of the absolute paths of the special files in the given directory
    """
    filenames = os.listdir(a_dir)
    file_list = []
    for filename in filenames:
        if ((not os.path.isdir(filename)) and is_special_path(filename)):
            a_path = os.path.join(a_dir, filename)
            absolute_path = os.path.abspath(a_path)
            file_list.append(absolute_path)
    return file_list


def get_special_paths_in_dirs(a_dirs):
    """
    return a list of the absolute paths of the special files in a list of directories
    """
    file_list = []
    for dirname in a_dirs:
        files_in_dirname = get_special_paths(dirname)
        # extend, not append
        file_list.extend(files_in_dirname)
    return file_list


def copy_to(paths, a_dir):
    """
    given a list of paths, copies those files into the given directory
    specification says use shutil
    """
    for path in paths:
        # copytree will copy a directory, not a file
        #shutil.copytree(path, a_dir)
        # copy2 will copy a file, not a directory
        shutil.copy2(path, a_dir)
