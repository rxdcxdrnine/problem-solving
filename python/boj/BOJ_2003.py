from typing import List


def solution(N: int, M: int, numbers: List[int]):

    count: int = 0

    for ind in range(N):
        if is_target(ind, ind):
            count += 1

        if is_target(ind, ind + 1):
            count += 1

    return count


def is_target(left: int, right: int):
    total: int = sum(numbers[left: right + 1])

    if left >= 0 and right < N and total == M:
        return True

    while left > 0 and right < N - 1 and \
            numbers[left - 1] + numbers[right + 1] + total <= M:

        left -= 1
        right += 1
        total += numbers[left] + numbers[right]

        if total == M:
            return True

    return False


if __name__ == "__main__":
    N, M = list(map(int, input().split()))

    numbers: List[int] = list(map(int, input().split()))

    print(solution(N, M, numbers))
