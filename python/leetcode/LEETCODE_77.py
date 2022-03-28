from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    visited: List[bool] = [False for _ in range(n + 1)]
    route: List[int] = []
    result: List[List[int]] = []

    def dfs(now: int):
        if len(route) == k:
            result.append(route[:])

        for dest in range(now + 1, n + 1):
            if visited[dest]:
                continue

            visited[dest] = True
            route.append(dest)
            dfs(dest)

            visited[dest] = False
            route.pop()

    dfs(0)
    return result


if __name__ == "__main__":
    print(combine(6, 3))
