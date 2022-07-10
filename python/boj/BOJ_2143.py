import collections
from typing import List, Dict


def solution(T: int, a: List[int], b: List[int]) -> int:
    count_a: Dict[int] = collections.defaultdict(int)
    count_b: Dict[int] = collections.defaultdict(int)

    for i in range(len(a)):
        tmp: int = 0
        for j in range(i, len(a)):
            tmp += a[j]
            count_a[tmp] += 1

    for i in range(len(b)):
        tmp: int = 0
        for j in range(i, len(b)):
            tmp += b[j]
            count_b[tmp] += 1

    total_a = sorted(count_a.keys())
    total_b = sorted(count_b.keys())
    result: int = 0

    left, right = 0, len(total_b) - 1
    while left < len(total_a) and right >= 0:
        if total_a[left] + total_b[right] == T:
            num_a, num_b = total_a[left], total_b[right]
            result += count_a[num_a] * count_b[num_b]
            left += 1
            right -= 1

        else:
            if total_a[left] + total_b[right] < T:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    T: int = int(input())
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    M: int = int(input())
    B: List[int] = list(map(int, input().split()))
    print(solution(T, A, B))
