import fileinput

number_list = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        number_list.append(int(line))
seen = set()
for number in number_list:
    if 2020-number in seen:
        print((2020-number)*number)
    seen.add(number)
