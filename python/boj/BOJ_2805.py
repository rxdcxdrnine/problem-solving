from typing import List


def solution(trees: List[int], M: int) -> int:

    def determination(value: int) -> bool:
        total: int = 0

        for tree in trees:
            if tree > value:
                total += tree - value

        return total >= M

    def binary_search(left: int, right: int) -> int:
        answer: int = 0

        while left <= right:
            mid: int = (left + right) // 2
            if determination(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

    return binary_search(0, 1_000_000_000)


if __name__ == "__main__":
    N, M = map(int, input().split())
    trees: List[int] = list(map(int, input().split()))

    print(solution(trees, M))
