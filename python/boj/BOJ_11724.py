import collections
from typing import List, Dict


def solution(n: int, edges: List[List[int]]):

    graph: Dict[int, List] = collections.defaultdict(list)
    visited: List[bool] = [False for _ in range(n)]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    stack = []
    answer: int = 0

    for vertex in range(1, n + 1):
        if visited[vertex - 1]:
            continue

        answer += 1
        stack.append(vertex)
        visited[vertex - 1] = True

        while stack:
            now: int = stack.pop()

            for dest in graph[now]:
                if not visited[dest - 1]:
                    stack.append(dest)
                    visited[dest - 1] = True

    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges: List[List[int]] = []

    for _ in range(m):
        edges.append(list(map(int, input().split())))

    print(solution(n, edges))
