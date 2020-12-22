import numpy as np
from sympy import cos,sin,pi # just to get exact values for cos(pi) and similar
from sys import exit

# Store input as a list of strings
#with open("small_input.txt") as f:
with open("input.txt") as f:
    moves = f.read().splitlines()

# I could transform F into the actual direction, then sum all numbers for each direction, and get the answer

#do matrix mult of unitary vectors
all_dir = dict([('E', (1,0)), ('N', (0,1)), ('W', (-1,0)),('S',(0,-1))])
my_inverted_dict = dict(map(reversed, all_dir.items()))

curr_dir = 'E'
coord = np.array([0,0])
for move in moves:
    direc = move[0]
    unit = int(move[1:])
    if direc == 'F':
        direc = curr_dir
    if direc == 'R':
        unit = unit*pi/180
        rotmat = [[cos(unit),-sin(unit)],[sin(unit),cos(unit)]]
        new_dir_val = tuple(np.matmul(all_dir[curr_dir],rotmat))
        curr_dir = my_inverted_dict[new_dir_val]
    elif direc == 'L':
        unit = unit*pi/180
        rotmat = [[cos(unit),+sin(unit)],[-sin(unit),cos(unit)]]
        new_dir_val = tuple(np.matmul(all_dir[curr_dir],rotmat))
        curr_dir = my_inverted_dict[new_dir_val]
    elif direc == 'E':
        coord += (unit,0)
    elif direc == 'N':
        coord += (0,unit)
    elif direc == 'W':
        coord += (-unit,0)
    elif direc == 'S':
        coord += (0,-unit)
print(abs(coord[0])+abs(coord[1]))
