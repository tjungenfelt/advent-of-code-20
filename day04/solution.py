import fileinput
import re

pps = []
with fileinput.input('input.txt') as f:
    for line in f:
        pps.append(line.split())
requirements = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

# PART 1
i = 0
seen = set()
for line in pps:
    if not line:
        if requirements.issubset(seen):
            i += 1
        seen = set()
    for element in line:
        key = element.split(":")[0]
        seen.add(key)
if requirements.issubset(seen):
    i += 1
print(i)


# PART 2

def is_valid(key, value):
    year_pattern = re.compile("^([0-9]{4})$")
    height_pattern = re.compile("^([1-9])([0-9]*)(cm|in)$")
    color_pattern = re.compile("^#([0-9a-z]{6})$")
    pid_pattern = re.compile("^([0-9]{9})$")
    if key == "byr":
        return year_pattern.match(value) and value.isnumeric() and 1920 <= int(value) <= 2002
    elif key == "iyr":
        return year_pattern.match(value) and value.isnumeric() and 2010 <= int(value) <= 2020
    elif key == "eyr":
        return year_pattern.match(value) and value.isnumeric() and 2020 <= int(value) <= 2030
    elif key == "hgt":
        if not height_pattern.match(value):
            return False
        if value.endswith("cm"):
            return 150 <= int(value.rstrip("cm")) <= 193
        elif value.endswith("in"):
            return 59 <= int(value.rstrip("in")) <= 76
    elif key == "hcl":
        return color_pattern.match(value)
    elif key == "ecl":
        return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    elif key == "pid":
        return pid_pattern.match(value)
    else:
        return True


i = 0
seen = set()
for line in pps:
    if not line:
        if requirements.issubset(seen):
            i += 1
        seen = set()
    for element in line:
        key, value = element.split(":")
        if is_valid(key, value):
            seen.add(key)
if requirements.issubset(seen):
    i += 1
print(i)