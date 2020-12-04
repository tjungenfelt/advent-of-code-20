import fileinput

pw_list = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        pw_list.append(line.rstrip())

# PART 1
i = 0
for row in pw_list:
    policy, password = row.split(":")
    interval, letter = policy.split()
    low, high = interval.split("-")
    occurrences = password.count(letter)
    if int(low) <= occurrences <= int(high):
        i += 1
print(i)

# PART 2
i = 0
for row in pw_list:
    policy, password = row.split(": ")
    interval, letter = policy.split()
    low, high = interval.split("-")
    if (password[int(low)-1] == letter) ^ (password[int(high)-1] == letter):
        i += 1
print(i)
