#!/usr/bin/python

adapters = set(int(line.strip()) for line in open('input.txt'))

jolt = 0

one_diff = 0
three_diff = 1 #Device adapter is always a three

while (len(adapters) > 0):

   jolt += 1


   if (jolt in adapters):

       one_diff += 1

   else:

       jolt += 2
       three_diff += 1
  
   adapters.remove(jolt) 

print(one_diff * three_diff)
