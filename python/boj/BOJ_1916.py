import collections
import heapq
from typing import List, Dict


def solution(start: int, end: int, edges: List[List[int]]):

    graph: Dict[int, List[List[int]]] = collections.defaultdict(list)

    for edge in edges:
        depart, arrive, cost = edge
        graph[depart].append([arrive, cost])

    dist: Dict[int, int] = collections.defaultdict(int)
    queue: List[List[int]] = [[0, start]]

    while queue:
        total, now = heapq.heappop(queue)
        if now in dist:
            continue

        dist[now] = total
        for dest, cost in graph[now]:
            alt: int = total + cost
            heapq.heappush(queue, [alt, dest])

    return dist[end]


if __name__ == "__main__":
    N: int = int(input())
    M: int = int(input())
    edges: List[List[int]] = []  # [depart, arrive, cost]

    for _ in range(M):
        edges.append(list(map(int, input().split())))

    start, end = list(map(int, input().split()))

    print(solution(start, end, edges))
