import sys
from typing import List


def solution(N: int, nums: List[int], rest: List[int]):
    routes: List[List[int]] = []

    def dfs(route: List[int]):

        if len(route) == N - 1:
            routes.append(route[:])

        for dest in range(len(rest)):
            if not rest[dest]:
                continue

            rest[dest] -= 1
            route.append(dest)
            dfs(route)

            rest[dest] += 1
            route.pop()

    dfs([])

    min_num: int = sys.maxsize
    max_num: int = -sys.maxsize

    def operate(left: int, right: int, op: int):
        if op == 0:
            return left + right
        elif op == 1:
            return left - right
        elif op == 2:
            return left * right
        else:
            if left * right < 0:
                return -(abs(left) // abs(right))
            return left // right

    for route in routes:
        stack: List[int] = list(reversed(nums))
        ops: List[int] = list(reversed(route))

        while len(stack) != 1:
            left: int = stack.pop()
            right: int = stack.pop()
            op: int = ops.pop()

            stack.append(operate(left, right, op))

        min_num = min(min_num, stack[0])
        max_num = max(max_num, stack[0])

    return min_num, max_num


if __name__ == "__main__":
    N: int = int(input())
    nums: List[int] = list(map(int, input().split()))
    rest: List[int] = list(map(int, input().split()))

    min_num, max_num = solution(N, nums, rest)

    print(max_num)
    print(min_num)
