from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    route: List[int] = []
    result: List[List[int]] = []

    dfs(candidates, route, result, 0, target)
    return result


def dfs(nums: List[int], route: List[int], result: List[List[int]],
        now: int, target: int) -> None:

    if sum(route) == target:
        result.append(route[:])

    for dest in range(now, len(nums)):
        if sum(route) + nums[dest] > target:
            continue

        route.append(nums[dest])
        dfs(nums, route, result, dest, target)

        route.pop()


if __name__ == "__main__":
    print(combinationSum([2, 3, 6, 7], 7))
