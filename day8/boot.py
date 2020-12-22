import numpy as np

# Store input as a list of strings
with open("input.txt") as f:
    lines = f.read().splitlines()

idx = 0
acc = 0
idx_list = []

while True:
    if idx in idx_list:
        print("Infinite loop!")
        break
    idx_list.append(idx)
    line = lines[idx]
    key = line[:3]
    value = int(line[4:])
    #print(key,value)
    if key == 'acc':
        acc += value
        idx += 1
    elif key == 'jmp':
        idx += value
    elif key == 'nop':
        idx += 1

print(acc)
