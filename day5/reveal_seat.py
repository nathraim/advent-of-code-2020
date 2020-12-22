# Store input as a list of strings
with open("input.txt") as f:
    lines = f.read().splitlines()

def get_row_or_column(subcode,nb,char1,char2):
    # subcode is the portion of code related to either rows or columns, 2^nb is the number of rows or columns
    # Define initial interval [inf,sup], which will get halved each step
    inf = 0
    sup = 2**nb - 1
    for letter in subcode:
        if letter == char1:
            sup = (sup + inf - 1)//2 # Take lower part
        elif letter == char2:
            inf = (sup + inf + 1)//2 # Take upper part
    return inf # Note: inf=sup at the end of the loop

def get_id(code,nbrow,nbcolumn):
    row = get_row_or_column(code[:nbrow],nbrow,'F','B')
    column = get_row_or_column(code[nbrow:],nbcolumn,'L','R')
    return 8*row + column # unique id. I think the 8 should be changed to nb_row+1 to be general

id_list = [get_id(code,7,3) for code in lines] # In the present case, there are 2^7 rows and 2^3 columns

max_id = max(id_list)
print('Max id: ',max_id)

# Part 2 of the puzzle

min_id = min(id_list)
# Calculate theoretical sum of all ids if none were missing
sum_id_th = (max_id + min_id)*(max_id + 1 - min_id)//2
# The missing id is then the difference between the theoretical and actual sum
my_id = sum_id_th - sum(id_list)

print('My id: ',my_id)
