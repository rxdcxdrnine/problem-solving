import collections
from typing import List, Dict, Deque


def solution(n: int, edges: List[List[int]]) -> List[int]:
    graph: Dict[int, List[int]] = collections.defaultdict(list)
    indegree: List[int] = [0 for _ in range(n + 1)]

    for start, end in edges:
        graph[start].append(end)
        indegree[end] += 1

    queue: Deque[int] = collections.deque()
    result: List[int] = []

    for ind in range(1, n + 1):
        if indegree[ind] == 0:
            queue.append(ind)

    while queue:
        now: int = queue.popleft()
        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1

            if indegree[node] == 0:
                queue.append(node)

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    paths: List[List[int]] = []

    for _ in range(M):
        paths.append(list(map(int, input().split())))

    answer: List[int] = solution(N, paths)
    print(' '.join(map(str, answer)))
