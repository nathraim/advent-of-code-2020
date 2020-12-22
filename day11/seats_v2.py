import numpy as np
from sys import exit
import time

# Store input as a list of strings
with open("input.txt") as f:
    seats = f.read().splitlines()
for i,el in enumerate(seats):
    seats[i] = [seat for seat in el]

seats_new = np.copy(seats) # Creates a copy of seats

def is_adjacent_free(seats,i,j):
    nocc = 0
    for k in [i-1,i,i+1]:
        for l in [j-1,j,j+1]:
            if k >= 0 and k < len(seats) and l >= 0 and l < len(seats[0]) and (k!=i or l!=j) and seats[k][l] == '#': 
                nocc += 1
    return nocc

# I should do a dict of functions here! Then loop through dir_list and call the dict to increment indexes
def next_index(i,j,string):
    if string == 'u': 
        i -= 1
    elif string == 'ul': 
        i -= 1 ; j -= 1
    elif string == 'l': 
        j -= 1 
    elif string == 'dl': 
        i += 1 ; j -= 1
    elif string == 'd': 
        i += 1
    elif string == 'dr': 
        i += 1 ; j += 1
    elif string == 'r': 
        j += 1 
    elif string == 'ur': 
        i -= 1 ; j += 1
    return i,j

def is_idx_bounded(k,l,seats):
    if k >= 0 and k < len(seats) and l >= 0 and l < len(seats[0]): 
        return True
    else:
        return False

def nb_direction_free(seats,i,j):
    dir_list = ['u','ul','l','dl','d','dr','r','ur']
    nocc = 0
    for direc in dir_list:
        k,l = next_index(i,j,direc)
        while is_idx_bounded(k,l,seats):
            if seats[k][l] == '#':
                nocc += 1
                break
            elif seats[k][l] == 'L':
                break
            k,l = next_index(k,l,direc)
    return nocc

def occupy_seats(seats,seats_new):
    for i,row in enumerate(seats):
        for j,seat in enumerate(row):
            start = time.time()
            #if seat == 'L' and nb_direction_free(seats,i,j) == 0:
            if seat == 'L' == 0:
                seats_new[i][j] = '#'
            #elif seat == '#' and nb_direction_free(seats,i,j) >= 5:
            elif seat == '#':
                seats_new[i][j] = 'L'
            end = time.time()
            print(100000*(end-start))
    return seats_new

def count_occ(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def print_seats(seats):
    for row in seats:
        for seat in row:
            print(seat,end='')
        print('')
    print('\n')

#print_seats(seats_new)

seats_new = occupy_seats(seats,seats_new)
#print_seats(seats_new)

exit()

count_iter = 1
while ((seats_new != seats).any()):
    count_iter += 1
    seats = np.copy(seats_new)
    seats_new = occupy_seats(seats,seats_new)
    #print_seats(seats_new)

print('After',count_iter, 'iterations, there are',count_occ(seats), 'occupied seats')

