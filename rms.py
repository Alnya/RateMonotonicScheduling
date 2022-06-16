from math import ceil


def judge(task, s, i):
    for ss in s:
        k, l = ss
        v = 0
        for j in range(1, i + 1):
            cj = task[j - 1][1]
            tk = task[k - 1][0]
            tj = task[j - 1][0]
            v += cj * (1 / (l * tk)) * ceil((l * tk) / tj)
        if v <= 1:
            return True
    return False


def rms(n, task):
    s = [[] for _ in range(n)]
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            for l in range(1, ceil(task[i - 1][0] / task[k - 1][0]) + 1):
                s[i - 1].append([k, l])
    for i in range(1, len(s) + 1):
        ok = judge(task, s[i - 1], i)
        if not ok:
            return False
    return True


def main():
    n = int(input("タスクの個数nを入力："))
    task = []
    for i in range(n):
        task.append(list(map(int, input(f"タスク{i + 1}の要素(空白区切り)：").split())))
    if rms(n, task):
        print("スケジューリング可能")
    else:
        print("スケジューリング不可能")


if __name__ == '__main__':
    main()
