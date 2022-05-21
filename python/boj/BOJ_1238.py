import collections
import heapq
from typing import List, Dict, Tuple, Optional


def dijkstra(n: int, start: int, graph: Dict[int, List[Tuple[int, int]]]) -> List[int]:
    dist: List[Optional[int]] = [None for _ in range(n + 1)]
    queue: List[Tuple[int, int]] = [(0, start)]  # [cost, now]

    while queue:
        cost, now = heapq.heappop(queue)

        if dist[now] is not None:
            continue

        dist[now] = cost
        for dest, weight in graph[now]:
            alt: int = cost + weight
            heapq.heappush(queue, (alt, dest))

    dist[0] = 0
    return dist


def solution(n: int, x: int, paths: List[List[int]]) -> int:
    graph: Dict[int, List[Tuple[int, int]]] = collections.defaultdict(list)

    for start, end, cost in paths:
        graph[start].append((end, cost))

    dists: List[List[int]] = []

    for start in range(1, n + 1):
        dist: List[int] = dijkstra(n, start, graph)
        dists.append(dist)

    depart: List[int] = [0] + [dist[x] for dist in dists]
    arrive: List[int] = dists[x - 1]

    result: List[int] = [0 for _ in range(n + 1)]
    for i, (num_d, num_a) in enumerate(zip(depart, arrive)):
        result[i] = num_d + num_a

    return max(result)


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    arr: List[List[int]] = []

    for _ in range(M):
        arr.append(list(map(int, input().split())))
    print(solution(N, X, arr))
