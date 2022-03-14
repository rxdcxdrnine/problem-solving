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

    for dest in range(now + 1, n + 1):
        if visited[dest]:
            continue

        visited[dest] = True
        route.append(dest)
        dfs(n, k, dest, count + 1, visited, route, result)

        visited[dest] = False
        route.pop()


if __name__ == "__main__":
    print(combine(1, 1))
