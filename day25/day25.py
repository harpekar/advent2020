#!/usr/bin/python

public_keys = list(int(line.strip()) for line in open('input.txt'))

divisor = 20201227 #Magic number given in problem prompt

subj_num = 7

loop_size = 0

door_key = 1

while (door_key != public_keys[0]):

   loop_size += 1

   door_key = (door_key * subj_num) % divisor 

card_key = public_keys[1]   

enc_key = 1

for i in range(loop_size): 
    enc_key = (enc_key * card_key) % divisor


print(enc_key)
