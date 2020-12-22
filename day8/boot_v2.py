import numpy as np

# Store input as a list of strings
with open("input.txt") as f:
    lines = f.read().splitlines()

idx = 0
acc = 0
idx_list = []
jmp_list = []
first = True
count = 0

while idx != len(lines):
    if idx in idx_list:
        #print("Infinite loop! Trying another modification")
        acc = acc_backup
        idx = idx_backup
        idx_list = idx_list_backup.copy()
        first = True
        count +=1
    idx_list.append(idx)
    line = lines[idx]
    key = line[:3]
    value = int(line[4:])
    if key == 'acc':
        acc += value
        idx += 1
    elif key == 'jmp' and first == True:
        first = False
        idx_bad = idx
        acc_backup = acc
        idx_backup = idx + value # In case this is not he correct jmp to modify, we want to start from the index it points to, otherwise we get stuck modifying the same jmp over and over: an infinite loop inside the infinite loop! :D
        idx_list_backup = idx_list.copy()
        idx += 1 # Do as if it were a 'nop'
    elif key == 'jmp':
        idx += value
    elif key == 'nop':
        idx += 1

print('Hurray! acc=', acc, 'bad jmp instruction was at line ', idx_list_backup[-1]+1)
