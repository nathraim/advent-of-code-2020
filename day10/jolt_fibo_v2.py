import numpy as np
import sys

adapters = np.loadtxt("input.txt",dtype='int')

adapters = np.sort(adapters)
adapters = np.insert(adapters,0,0) # Add charging outlet in 1st position (it has 0 joltage)

# Create a list nb_path that will in the end contain the number of possible different connections (=paths) for a given adapter.
# An index of nb_path corresponds to a given adapter, and so corresponds to the same index as in adapters.
nb_path = [0 for i in range(len(adapters))]
lp = len(nb_path)
# The last adapter always has only 1 possible path
nb_path[-1] = 1

# For a given adapter, determine how many adapters it can directly connect to, i.e., determine its number of neighbors (upwards).
for i,el in enumerate(adapters):
    for j,el2 in enumerate(adapters[i+1:i+4]): # Nath: actually...why doesn't it crash when i+4 gets larger than len(adapters)?
        if el2-el <= 3 :
            nb_path[i]+=1

# Now is Fibonaccci time (with 3 'c' because in this case it's the sum of up to 3 previous terms). We loop through nb_path backwards. But it's not really Fibonacci, because we don't always sum the 3 previous terms...
# The number of possible arrangements starting from a given adapter will simply be the sum of the possible arrangements for the (up to) 3 previous adapters.
for i,el in enumerate(list(reversed(nb_path))):
    if i < 3:
        pass
    else:
        nb = 0
        for j in range(el):
            nb += nb_path[lp-i+j]
        nb_path[lp-1-i] = nb

print('arrangements:', nb_path[0])

# Comments:
# This is much shorter than the other method that defines a list of neighbors, and finds recursively the number of paths.
# But the other method is more general! The principle would work for any type of graph, actually, no matter the maximum number of connections,
# no matter if what links the nodes/adapters are integers, etc. It would also allow me to give the actual arrangements, and not just the numbers.
# Here however, I take advantage of the fact that we just want the NUMBER of arrangements! And I take advantage of the fact that a node is connected to max 3 other nodes. I also use the fact that the adapters can be sorted as an increasing integers list, so that we cannot "go back" to an adapter with lower value.

# It is actually here a 1-dimensional graph, which can be represented on a single axis.
# Last note: In principles I should determine "by hand" the last 3 values of nb_path, that is, find the true number of arrangements for the last 3 entries of nb_path.
# But here we are lucky. Last element is 1. The second to last is necessarily 1. And the third to last is either 2 or 1. In other terms, the number of arrangements for each of the last 3 terms is equal to their number of connections...
