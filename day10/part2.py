#!/usr/bin/python

import itertools

adapters = [int(line.strip()) for line in open('input.txt')]

adapters.sort()

adapters.insert(0,0) #Start with the 0 jolt wall power

tribonacci = [1,1,2] 



arrangements = 1 #The first arrangement is with all adapters 

path_num = 1

seg_len = 0

def tribo(ind):
    for i in range(3, (ind+1)):
        tribonacci.append(sum(tribonacci[(i-3):i]))

    return tribonacci[ind]                

for i in range(len(adapters)):

    print(adapters[i])

    #print("Next adapter is ", next(adapters))

    if ((i == len(adapters) - 1)) or ((adapters[i+1]) is (3 + adapters[i])):

        if (seg_len in range(len(tribonacci))):
            path_num = tribonacci[seg_len]
        
        else:    
            path_num = tribo(seg_len) 
       
        print("Path num is ", path_num)         

        arrangements *= path_num #Each path possibility multiplies the possible arrangements

        print("Total arrangements is ", arrangements)

        seg_len = 0

    else:
        seg_len += 1  

        print("Segment length is ", seg_len) 


print('\n')

print(arrangements)   
