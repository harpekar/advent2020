#!/usr/bin/python

import re

x_pos = 0
total_trees = 0

with open('input.txt', 'r') as slope:
    for line in slope.readlines():

        if line[x_pos % (len(line) - 1)] == '#':
                total_trees = total_trees + 1

        x_pos = x_pos + 3


print(total_trees)
