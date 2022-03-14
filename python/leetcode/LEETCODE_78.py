from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    visited: List[bool] = [False for _ in nums]
    route: List[int] = []
    result: List[List[int]] = []

    dfs(nums, -1, visited, route, result)
    return result


def dfs(nums: List[int], now: int,
        visited: List[int], route: List[int], result: List[List[int]]) -> None:
    result.append(route[:])

    for dest in range(now + 1, len(nums)):
        if visited[dest]:
            continue

        visited[dest] = True
        route.append(nums[dest])
        dfs(nums, dest, visited, route, result)

        visited[dest] = False
        route.pop()


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
