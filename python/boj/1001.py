from typing import List, Tuple


def solution(a: int, b: int):
    remains: List[int] = []
    rest: int = a % 10

    for _ in range(b):
        remains.append(rest)
        rest = (rest * a) % 10

        if rest in remains:
            break

    answer: int = remains[b % len(remains) - 1]
    print(remains, b % len(remains))
    return answer if answer != 0 else 10


if __name__ == "__main__":
    n = int(input())
    data: List[Tuple[int, int]] = []

    for i in range(n):
        data.append(list(map(int, input().split())))

    for i in range(n):
        a, b = data[i]
        print(solution(a, b))
