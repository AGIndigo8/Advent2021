#%
import numpy as np
import math

def sigma(x):
    return sum(range(x+1))

with open('data.txt') as f:
    input = f.read()
input = [int(x) for x in input.split(',')]
mi= max(input)
print(mi)
all_dist=[sum([sigma(abs(x-a)) for x in input]) for a in range(mi+1)]
print([x for pos,x in enumerate(all_dist) if x == min(all_dist)])
