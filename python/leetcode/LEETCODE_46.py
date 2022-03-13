from typing import List


def permute(nums: List[int]):
    visited: List[int] = [False for _ in range(len(nums))]
    route: List[int] = []
    result: List[List[int]] = []

    dfs(nums, 0, visited, route, result)
    return result


def dfs(nums: List[int], count: int, visited: List[int],
        route: List[int], result: List[List[int]]):

    if count == len(nums):
        result.append(route[:])
        return

    for ind in range(len(nums)):
        if visited[ind]:
            continue

        visited[ind] = True
        route.append(nums[ind])
        dfs(nums, count + 1, visited, route, result)

        visited[ind] = False
        route.pop()


if __name__ == "__main__":
    print(permute([1, 2, 3]))
