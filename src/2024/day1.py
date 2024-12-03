def get_input():
    c1 = []
    c2 = []
    with open("data/2024/day1") as f:
        for line in f:
            c = line.split()
            c1.append(int(c[0]))
            c2.append(int(c[1]))
    return c1, c2


def solve():
    s = 0
    c1, c2 = get_input()
    c1.sort()
    c2.sort()
    for i in range(len(c1)):
        s += abs(int(c1[i]) - int(c2[i]))
    print(s)


def solve2():
    c1, c2 = get_input()
    c2_q = {}
    for i in c2:
        if i in c2_q:
            c2_q[i] += 1
        else:
            c2_q[i] = 1
    s = 0
    for j in c1:
        sm = c2_q.get(j, 0)
        sm *= j
        s += sm
    print(s)
