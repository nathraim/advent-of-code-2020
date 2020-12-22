import numpy as np
from sys import exit

# Store input as a list of strings
with open("small_input.txt") as f:
#with open("input.txt") as f:
    seats = f.read().splitlines()
for i,el in enumerate(seats):
    seats[i] = [seat for seat in el]

seats_new = np.copy(seats) # Creates a copy of seats

def print_seats(seats):
    for row in seats:
        for seat in row:
            print(seat,end='')
        print('')
    print('\n')

seats_subpart = [row[1:4] for row in seats[2:5]]
print_seats(seats)
print_seats(seats_subpart)
exit()

def nb_adjacent_occ(seats,i,j):
    nocc = 0
    for k in [i-1,i,i+1]:
        for l in [j-1,j,j+1]:
            if k >= 0 and k < len(seats) and l >= 0 and l < len(seats[0]) and (k!=i or l!=j) and seats[k][l] == '#': 
                nocc += 1
    return nocc

def occupy_seats(seats,seats_new):
    for i,row in enumerate(seats):
        for j,seat in enumerate(row):
            if seat == 'L' and nb_adjacent_occ(seats,i,j) == 0:
                seats_new[i][j]='#'
            elif seat == '#' and nb_adjacent_occ(seats,i,j) >= 4:
                seats_new[i][j]='L'
    return seats_new

def count_occ(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1
    return count

#print(seats_new,'\n')
seats_new = occupy_seats(seats,seats_new)
#print(seats_new,'\n')

count_iter = 1
while ((seats_new != seats).any()):
    count_iter += 1
    seats = np.copy(seats_new)
    seats_new = occupy_seats(seats,seats_new)
    #print(seats_new,'\n')

print('After',count_iter, 'iterations, there are',count_occ(seats), 'occupied seats')

            
