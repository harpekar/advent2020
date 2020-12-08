#!/usr/bin/python

import re

curr_pass = {}

valid_pass = 0

requ_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #Country ID is not required

def is_legit(curr_pass):

    for field in requ_fields:

        value = curr_pass.get(field)
        
        if (value is None): #Value does not exist
            return False;
        
        elif (field == 'byr'):
            if ((int(value) in range(1920, 2003)) is False): 
                return False;
        elif (field == 'iyr'):
            if ((int(value) in range(2010, 2021)) is False):  
                return False;
        elif (field == 'eyr'):
            if ((int(value) in range(2020, 2031)) is False):  
                return False;
        elif (field == 'hgt'):
            if (re.match('((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)', value) is None): #150-193 cm or 59-76 in  
                return False;                     
        elif (field == 'hcl'):
            if (re.match('^#[0-9a-f]{6}$',value) is None): #Match to any # + 6 digits                
                return False;
        elif (field == 'ecl'):
            if ((value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) is False):
                return False;   
        else: 
            if (re.match('^[0-9]{9}$',value) is None):
                return False;

    return True;


with open('input.txt', 'r') as lines:
    for line in lines.readlines():
        if (line == '\n'):

            if (is_legit(curr_pass)):
                valid_pass = valid_pass + 1

            curr_pass = {} #Clear passport after determining its legitimacy
        
        else: #Concatenate each password into a single string 
            
            line_parts = line.rstrip("\n").split(" ")

            for part in line_parts:

                key, value = part.split(":")

                curr_pass.update({key: value})
                
print(valid_pass)
