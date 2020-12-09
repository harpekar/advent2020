#!/usr/bin/python

import re

group_ans = set()

score = 0

with open('input.txt', 'r') as lines:
    for line in lines.readlines():
        if (line == '\n'):
            
            score = score + len(group_ans)

            group_ans = set() #Clear passport after determining its legitimacy
        
        else:  
            chars = set(line.rstrip("\n"))

            group_ans |= chars #Add unique characters from each line 
                
print(score)
