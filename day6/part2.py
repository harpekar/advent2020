#!/usr/bin/python

import re
import string

group_ans = set(string.ascii_lowercase) #Set of all letters, to start

score = 0

with open('input.txt', 'r') as lines:
    for line in lines.readlines():
        if (line == '\n'):
            
            score = score + len(group_ans)

            #Reset potential answer pool
            group_ans = set(string.ascii_lowercase) 
        
        else:  
            chars = set(line.rstrip("\n"))

            group_ans = group_ans & chars #Only the characters in every line

                
print(score)
