import fileinput
import itertools

number_list = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        number_list.append(int(line))

# PART 1
seen = set()
for number in number_list:
    if 2020-number in seen:
        print((2020-number)*number)
    seen.add(number)

# PART 2
comb_list = list(itertools.combinations(number_list, 3))
for combination in comb_list:
    x, y, z = combination
    if x+y+z == 2020:
        print(x*y*z)
