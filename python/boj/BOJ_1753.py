import collections
import heapq
from typing import List, Tuple, Dict, Optional


def solution(V: int, K: int, paths: List[List[int]]) -> List[Optional[int]]:
    graph: Dict[int, List[Tuple[int, int]]] = collections.defaultdict(list)

    for start, end, cost in paths:
        graph[start].append((end, cost))

    queue: List[Tuple[int, int]] = [(0, K)]
    dist: List[Optional[int]] = [None for _ in range(V + 1)]
    dist[0] = 0

    while queue:
        cost, now = heapq.heappop(queue)

        if dist[now] is not None:
            continue

        dist[now] = cost
        for dest, weight in graph[now]:
            alt: int = cost + weight
            heapq.heappush(queue, (alt, dest))

    return dist[1:]


if __name__ == "__main__":
    V, E = map(int, input().split())
    K: int = int(input())

    paths: List[List[int]] = []
    for _ in range(E):
        paths.append(list(map(int, input().split())))

    dist: List[Optional[int]] = solution(V, K, paths)

    for num in dist:
        if num is None:
            print("INF")
        else:
            print(num)
