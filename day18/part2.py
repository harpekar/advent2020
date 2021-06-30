#!/usr/bin/python

import numpy

def compute_line(line):

    res = line.pop(0)

    mults = []

    if (res == "("): 
        res = compute_line(line)

    res = int(res)

    while(len(line) > 0):

        op = line.pop(0)
   
        if (op == ")"):
            break
        
        elif (op == "*"):
            mults.append(res)

            res = line.pop(0)

            if (res == "("):
                res = compute_line(line)

            res = int(res)

            continue
        else:

            second = line.pop(0)
        
            if (second == "("):
                second = compute_line(line)

            second = int(second)

            res += second


    mults.append(res)        

    result = numpy.prod(mults)

    return result   


hw_sum = 0

with open('input.txt', 'r') as lines:
    for line in lines.readlines():
        vals = list(line.strip().replace(" ", ""))
        
        res = compute_line(vals)  
       
        hw_sum += res


print(hw_sum)
