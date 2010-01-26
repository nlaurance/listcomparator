#!/usr/bin/python
# -*- coding: UTF8 -*-

from difflib import unified_diff
from os import path
import sys

HELP = """
compares 2 csv files and outputs delta as file_suppr.csv and file_addon.csv
usage : %s old_filename new_filenane
""" % sys.argv[0]


def sortir_ecart(old_file, new_file):
    """ compares 2 xml files
    """
    unused, filename = path.split(new_file)
    filename, unused = path.splitext(filename)

    old_file = open(old_file).readlines()
    new_file = open(new_file).readlines()
    ecart = list(unified_diff(old_file, new_file))
    ecart = ecart[4:-1]
    suppr = filter(lambda x: x.startswith('-'), ecart)
    addon = filter(lambda x: x.startswith('+'), ecart)

    suppr_file = open(filename + '_suppr.csv', 'w')
    for line in suppr:
        suppr_file.write(line[1:])
    suppr_file.close()

    addon_file = open(filename + '_addon.csv', 'w')
    for line in addon:
        addon_file.write(line[1:])
    addon_file.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print HELP
        sys.exit(1)
    else:
        sortir_ecart(args[1], args[2])
        sys.exit(0)
