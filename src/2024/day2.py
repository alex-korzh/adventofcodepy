def get_input():
    data = []
    with open("data/2024/day2") as f:
        for line in f:
            data.append(list(map(int, line.split())))

    return data


def is_safe(report: list[int]) -> bool:
    prev_diff = None
    for i, level in enumerate(report):
        if i == 0:
            continue
        diff = level - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            # print(f"Report {report} is unsafe: {diff=} is not between 1 and 3")
            return False
        if prev_diff and diff * prev_diff <= 0:
            # print(
            #     f"Report {report} is unsafe: {diff=} and {prev_diff=} are not of the same sign"
            # )
            return False
        prev_diff = diff
    # print(f"Report {report} is safe")
    return True


def solve():
    sn = 0
    for report in get_input():
        if is_safe(report):
            sn += 1
    print(sn)


def solve2():
    sn = 0
    for report in get_input():
        if is_safe(report):
            sn += 1
        else:
            for i in range(len(report)):
                tr = report[:i] + report[i + 1 :]
                if is_safe(tr):
                    sn += 1
                    break
    print(sn)


if __name__ == "__main__":
    solve2()
