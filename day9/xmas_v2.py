import numpy as np
from itertools import combinations

# Store input as a numpy array of ints
input_list = np.loadtxt("input.txt",dtype='int')

for idx,el in enumerate(input_list[25:]):
    # Make all possible combinations of 2 elements taken at most 25 indices before the current index
    l_combinations = combinations(input_list[idx:idx+25],2)
    if el not in np.sum(list(l_combinations),axis=1):
        print('invalid',idx,el)
        invalid_nb = el
        break

#part 2

for size in range(2,len(input_list)): # Loop through possible sizes of the contiguous list (min size=2)
    #print('hoho',size) #to check execution speed
    #Create list of lists, each of them being of size 'size' and containing consecutive elements of the original list
    contiguous_lists = [input_list[idx:idx+size] for idx in range(len(input_list)-size)] # fast
    #contiguous_lists = [[input_list[i + j] for j in range(size)] for i in range(len(input_list)-size)] #slow
    #contiguous_lists = list(zip(input_list,input_list[size:])) #Doesn't take consecutive elements, except for size=1
    sum0 = np.sum(contiguous_lists,axis=1)
    if invalid_nb in sum0:
        sum0 = sum0.tolist() #Convert to python list just to be able to use the .index method...
        idx_weak = sum0.index(invalid_nb) #index of the list whose sum matches the invalid number found earlier
        print('Encryption weakness:',min(contiguous_lists[idx_weak])+max(contiguous_lists[idx_weak]))
        break
