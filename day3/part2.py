#!/usr/bin/python

import re

y_pos = 0


#the Key is x change / y change per line, Value is number of trees on that line
paths = {'1' :   0,
         '3' :   0,
         '5' :   0, 
         '7' :   0,
         '0.5' : 0}

with open('input.txt', 'r') as slope:
    for line in slope.readlines():
        
        for key, value in paths.items():
            
            if ((key == '0.5') and (y_pos % 2 == 1)): #One route only calculates every other line
                continue;

            elif line[int((y_pos * float(key)) % (len(line) - 1))] == '#':
                paths[key] = paths[key] + 1

        y_pos = y_pos + 1    

total_trees = 1  

for key, value in paths.items(): 
    total_trees = total_trees * value


print(total_trees)
