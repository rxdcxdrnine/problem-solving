from typing import List


def permute(nums: List[int]):
    visited: List[int] = [False for _ in range(len(nums))]
    route: List[int] = []
    result: List[List[int]] = []

    def dfs():
        if len(route) == len(nums):
            result.append(route[:])
            return

        for dest in range(len(nums)):
            if visited[dest]:
                continue

            visited[dest] = True
            route.append(nums[dest])
            dfs()

            visited[dest] = False
            route.pop()

    dfs()
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
