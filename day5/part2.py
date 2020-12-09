#!/usr/bin/python

import re

def find_position(board_pass, seat_range):

    if ((board_pass == 'F') or (board_pass == 'L')):  
        return seat_range[0]
    elif ((board_pass == 'B') or (board_pass == 'R')):
        return (seat_range[1] - 1)
    else:

        range_adj = ((seat_range[1] - seat_range[0]) / 2)

        if ((board_pass[0] == 'F') or (board_pass[0] == 'L')):
            seat_range[1] -= range_adj
        else:
            seat_range[0] += range_adj    

        return (find_position(board_pass[1:], seat_range)) #Pop off first character in string    


ids = set()

with open('input.txt', 'r') as plane:
    for line in plane.readlines():
        
        rows = [0,128]
        columns = [0,8]
            
        line = line.rstrip("\n")

        row_chars, column_chars = line[:7], line[7:]
        
        row_pos = find_position(row_chars, rows)
        col_pos = find_position(column_chars, columns) 

        seat_id = (row_pos) * 8 + (col_pos)        

        ids.add(seat_id)    

all_seats = set(range(0,(max(ids) + 1)))
    
print(all_seats.difference(ids))
