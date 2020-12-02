#!/usr/bin/python

import re

valid_pwds = 0

with open('input.txt', 'r') as passwords:
    for line in passwords.readlines():

        [low_ind, high_ind, char, password] = re.split(': | |-',line) #Parse line

        if ((password[int(low_ind) - 1] == char) ^ (password[int(high_ind) - 1] == char)):
            valid_pwds = valid_pwds + 1


print(valid_pwds)
