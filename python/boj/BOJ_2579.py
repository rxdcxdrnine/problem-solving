from typing import List


def solution(n: int, stairs: List[int]) -> int:

    answer: List[int] = [0 for _ in range(n + 1)]

    def recursion(m: int):
        if m == 0:
            return stairs[0]
        if m == 1:
            return stairs[1]
        if m == 2:
            return stairs[1] + stairs[2]
        if answer[m]:
            return answer[m]

        answer[m] = stairs[m] + max(recursion(m - 2), stairs[m - 1] + recursion(m - 3))
        return answer[m]

    return recursion(n)


if __name__ == "__main__":
    N: int = int(input())
    arr: List[int] = [0]

    for _ in range(N):
        arr.append(int(input()))

    print(solution(N, arr))
