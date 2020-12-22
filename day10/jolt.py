import numpy as np
from functools import lru_cache

# Load data into numpy array
adapters = np.loadtxt("myinput.txt",dtype='int')

adapters = np.sort(adapters)

adapters = np.insert(adapters,0,0) # Add charging outlet in 1st position (it has 0 joltage)
diff = adapters[1:]-adapters[:-1]

count1 = 0
count3 = 1 # There is always 3 jolts difference between the highest adapter and the built-in adapter
for el in diff:
    if el == 1:
        count1 += 1
    elif el == 3:
        count3 += 1

print(count1*count3)

# Part 2

# For each node (represented by the index of a list of length the original input), find neighbors, i.e. nodes it connects to (cannot go backwards)
neighbors_list = [[] for i in range(len(adapters))]
for i,el in enumerate(adapters):
    for j,el2 in enumerate(adapters[i+1:i+4]):
        if el2-el <= 3 :
            #neighbors_list[i].append(el2) # Stores neighbors as values...
            neighbors_list[i].append(i+j+1) # Stores neighbors as indices

# Define variable that will store the number of paths for a given node
global store_path_numbers
store_path_numbers= [0 for i in range(len(adapters))]

#@lru_cache(maxsize=None)
def path_recursive(neighbors_list,length):
    global store_path_numbers
    diff_length = length - len(neighbors_list) # to check at at which level of recursivity we are
    count = 0
    if len(neighbors_list)==1: # i.e when the last list of neighbors is empty
        store_path_numbers[diff_length] = 1
        return 1
    else:
        for node in neighbors_list[0]:
            if store_path_numbers[node] != 0: # Use existing values instead of recomputing
                count += store_path_numbers[node]
            else:
                count += path_recursive(neighbors_list[node-diff_length:],length) 
    # Once we have finished an iteration, we know the number of paths for a given node, so store it for reuse
    if (store_path_numbers[diff_length]==0):
        store_path_numbers[diff_length] = count

    return count

#print('neighbors\n',list(zip(range(len(adapters)),neighbors_list))) # [node,[neighbors]]
#print('path_numbers\n',list(zip(range(len(adapters)),store_path_numbers))) # [node, nb of paths for this node]

arrangements = path_recursive(neighbors_list,len(neighbors_list))
print(arrangements)
