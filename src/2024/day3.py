import re


def get_input():
    with open("data/2024/day3") as f:
        return f.read()


def solve():
    pattern_mul = r"mul\(\d{1,3},\d{1,3}\)"
    pattern_num = r"\d+"
    inp = get_input()
    matches = re.findall(pattern_mul, inp)
    res = 0
    for mul in matches:
        numbers = re.findall(pattern_num, mul)
        res += int(numbers[0]) * int(numbers[1])
    print(res)


def solve2():
    pattern_mul = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    pattern_num = r"\d+"
    inp = get_input()
    res = 0
    do = True
    for cmd in re.findall(pattern_mul, inp):
        if "do" in cmd and "don't" not in cmd:
            do = True
            continue
        elif "don't" in cmd:
            do = False
            continue
        if do:
            numbers = re.findall(pattern_num, cmd)
            res += int(numbers[0]) * int(numbers[1])
    print(res)
