import numpy as np
import re

# example = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

with open('input.txt', 'r') as f:
    example = f.read()

crates = example.split('\n\n')[0]
crates

# n_cols = max([int(i) for i in "".join(crates.split('\n')[-1].split())])
n_cols = int((len(crates.split('\n')[0]) + 1) / 4)

pattern = r'[\s*\[\]]'
cols = [[] for i in range(n_cols)]
for row in crates.split('\n')[:-1]:
    for col in range(n_cols):
        item = re.sub(pattern, '', row[col*4:(col+1)*4])
        if len(item) > 0:
            cols[col].append(item)
cols = [col[::-1] for col in cols]

for instruction in example.split('\n\n')[1].strip().split('\n'):
    digits = re.findall(r'\d+', instruction)
    _to = int(digits[2]) - 1
    _from = int(digits[1]) - 1
    _n = int(digits[0])

    for item in cols[_from][-_n:]:
        cols[_to].append(item)
    del cols[_from][-_n:]


print("".join([i[-1] for i in cols]))
