from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    visited: List[bool] = [False for _ in range(n + 1)]
    route: List[int] = []
    result: List[List[int]] = []

    dfs(n, k, 0, 0, visited, route, result)
    return result


def dfs(n: int, k: int, now: int, count: int,
        visited: List[int], route: List[int], result: List[List[int]]):
    if count == k:
        result.append(route[:])

    for num in range(now + 1, n + 1):
        if visited[num]:
            continue

        visited[num] = True
        route.append(num)
        dfs(n, k, num, count + 1, visited, route, result)

        visited[num] = False
        route.pop()


if __name__ == "__main__":
    print(combine(1, 1))
