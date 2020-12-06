import fileinput

group_answers = []
with fileinput.input('input.txt') as f:
    for line in f:
        group_answers.append(line.rstrip())
