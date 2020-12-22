import numpy as np
from itertools import combinations

# Store input as a numpy array of ints
input_list = np.loadtxt("input.txt",dtype='int')
for idx,el in enumerate(input_list[25:]):
    # Make all possible combinations of 2 elements taken at most 25 indices before the current index
    l_combinations = combinations(input_list[idx:idx+25],2)
    invalid_nb = 0
    invalid_nb = filter(lambda c: (c[0]+c[1]) == el, l_combinations)
    if invalid_nb == 0:
        print('invalid',idx,el)

    #if el not in np.sum(list(l_combinations),axis=1):
    #    print('invalid',idx,el)
    #    invalid_nb = el
    #    break

#print('invalid',invalid_nb)
#part 2

#for size in range(2,len(input_list)): # Loop through possible sizes of the contiguous list (min size=2)
#    for idx in range(len(input_list)-size): # Loop through indices of the full list
#        contiguous_list = input_list[idx:idx+size]
#        if invalid_nb==sum(contiguous_list):
#            print('Encryption weakness:',min(contiguous_list)+max(contiguous_list))
#            break
