"""
Part 1: Find the Elf carrying the most Calories. 
        How many total Calories is that Elf carrying?
Part 2: Find the top three Elves carrying the most Calories. 
        How many Calories are those Elves carrying in total?
"""

with open('input.txt', 'r') as f:
    text = f.read()

total_cals = [sum([int(food) for food in elf.strip().split('\n')])
              for elf in text.split('\n\n')]

# Part 1:
print(f"Part 1: {max(total_cals):,} calories, carried by Elf #{total_cals.index(max(total_cals)) + 1}")

top_3 = []
top_3_inds = []
for i in range(3):
    most_cals = max(total_cals)
    most_cals_ind = total_cals.index(most_cals)
    top_3.append(most_cals)
    top_3_inds.append(most_cals_ind)
    total_cals.pop(most_cals_ind)
print(
    f"Part 2: {sum(top_3):,} total calories carried by Elves {', '.join([str(i+1) for i in top_3_inds])}.")
