import numpy as np
from sympy import cos,sin,pi # just to get exact values for cos(pi) and similar
from sys import exit

# Store input as a list of strings
with open("input.txt") as f:
    moves = f.read().splitlines()

#do matrix mult of unitary vectors
all_dir = dict([('E', (1,0)), ('N', (0,1)), ('W', (-1,0)),('S',(0,-1))])

coord_ship = np.array([0,0])
coord_waypoint = np.array([10,1])
for move in moves:
    direc = move[0]
    unit = int(move[1:])
    if direc == 'F':
        coord_ship = coord_ship + unit*coord_waypoint
    elif direc == 'R':
        # I could use complex for rotations...
        unit = unit*pi/180
        rotmat = [[cos(unit),-sin(unit)],[sin(unit),cos(unit)]]
        coord_waypoint = np.matmul(coord_waypoint,rotmat)
    elif direc == 'L':
        unit = unit*pi/180
        rotmat = [[cos(unit),sin(unit)],[-sin(unit),cos(unit)]]
        coord_waypoint = np.matmul(coord_waypoint,rotmat)
    else:
        coord_waypoint = coord_waypoint + unit*np.array(all_dir[direc])

print(sum(abs(coord_ship)))
