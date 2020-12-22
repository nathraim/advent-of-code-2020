import numpy as np
from itertools import groupby
from collections import Counter
from functools import reduce
from operator import mul

adapters = np.loadtxt("minimal_input.txt",dtype='int')

l_sorted = np.sort(adapters)
l_sorted = np.insert(l_sorted,0,0) # Add charging outlet in 1st position (it has 0 joltage)
l_sorted = l_sorted.tolist() 

def n_cut(l_sorted):
    diff = (b-a for a,b in zip(l_sorted,l_sorted[1:])) 
    size = (len(list(g)) for k,g in groupby(diff) if k==1)
    perm = ((n-1)*n//2+1 for n in size)
    return reduce(mul,perm)

print(n_cut(l_sorted))
