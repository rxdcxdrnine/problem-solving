from typing import List


def solution(n: int, commands: List[List[int]]):

    trains: List[int] = [0 for _ in range(n)]

    for c in commands:
        i: int = c[1] - 1

        if c[0] == 1:
            trains[i] = trains[i] | (1 << (c[2] - 1))
        if c[0] == 2:
            trains[i] = trains[i] & ~(1 << (c[2] - 1))
        if c[0] == 3:
            trains[i] = (trains[i] << 1) & (2 ** 20 - 1)
        if c[0] == 4:
            trains[i] = trains[i] >> 1

    return len(set(trains))


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    commands: List[List[int]] = []

    for _ in range(m):
        commands.append(list(map(int, input().split())))

    print(solution(n, commands))
