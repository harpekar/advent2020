#!/usr/bin/python

import re

curr_pass = ""

valid_pass = 0

requ_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #Country ID is not required

with open('input.txt', 'r') as lines:
    for line in lines.readlines():

        if (line == '\n'):

            if all(field in curr_pass for field in requ_fields):
                valid_pass = valid_pass + 1 

            curr_pass = "" #Clear passport after determining its legitimacy
        
        else: #Concatenate each password into a single string 
            curr_pass = curr_pass + line
            print(curr_pass)
                
print(valid_pass)
