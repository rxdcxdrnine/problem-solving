from typing import List


def solution(budgets: List[int], limit: int) -> int:

    def determination(value: int) -> bool:
        total: int = 0

        for budget in budgets:
            if budget >= value:
                total += value
            else:
                total += budget

        return total <= limit

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

    result: int = binary_search(0, limit)

    if result == limit:
        return max(budgets)
    else:
        return result


if __name__ == "__main__":
    N: int = int(input())
    budgets: List[int] = list(map(int, input().split()))
    limit: int = int(input())

    print(solution(budgets, limit))
