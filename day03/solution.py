import fileinput

forrest = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        forrest.append(line.rstrip())

r_max = len(forrest[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(x_step, y_step):
    x = 0
    y = 0
    trees = 0
    while y < len(forrest):
        if forrest[y][x] == "#":
            trees += 1
        y += y_step
        x = (x + x_step) % r_max
    return trees

# PART 1
print(count_trees(3, 1))

# PART 2
print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
