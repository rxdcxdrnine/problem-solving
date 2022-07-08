import collections
import heapq
import sys
from typing import List, Dict


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]):

    graph: Dict[int, List[List[int]]] = collections.defaultdict(list)
    dist: Dict[int, Dict[int]] = {}

    for fare in fares:
        start, end, cost = fare
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    def dijkstra(start: int):
        queue = [[0, start]]
        dist[start] = collections.defaultdict(lambda: None)

        while queue:
            cost, now = heapq.heappop(queue)
            if now in dist[start]:
                continue

            dist[start][now] = cost
            for dest, weight in graph[now]:
                alt: int = cost + weight
                heapq.heappush(queue, [alt, dest])

    dijkstra(s)
    dijkstra(a)
    dijkstra(b)

    answer: int = sys.maxsize
    for node in range(1, n + 1):
        if dist[s][node] is None or dist[a][node] is None or dist[b] is None:
            continue

        total: int = dist[s][node]
        total += dist[a][node]
        total += dist[b][node]

        answer = min(answer, total)

    return answer


if __name__ == "__main__":
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
