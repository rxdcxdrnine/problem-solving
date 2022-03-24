import collections
from typing import List, Union, Dict


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:

    visited: List[bool] = [False for _ in range(numCourses)]
    checked: List[bool] = [False for _ in range(numCourses)]
    graph: Dict[int, List[int]] = collections.defaultdict(list)

    for arrive, depart in prerequisites:
        graph[depart].append(arrive)

    def dfs(now: int):
        for dest in graph[now]:
            if checked[dest]:
                continue

            if visited[dest]:
                return False

            visited[dest] = True

            if not dfs(dest):
                return False

            checked[dest] = True
            visited[dest] = False

        return True

    for now in range(numCourses):
        visited[now] = True

        if not dfs(now):
            return False

        visited[now] = False

    return True


if __name__ == "__main__":
    print(canFinish(2, [[1, 0], [0, 1]]))