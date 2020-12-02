#!/usr/bin/python

import re

valid_pwds = 0

with open('input.txt', 'r') as passwords:
    for line in passwords.readlines():

        [low_range, high_range, char, password] = re.split(': | |-',line) #Parse line

        result = "".join(re.findall("%s" % char, password)) #Determine number of given character

        if (len(result) in range(int(low_range),(int(high_range) + 1))):
            valid_pwds = valid_pwds + 1


print(valid_pwds)
