from typing import List

INF: int = int(1e9)


def solution(N: int, M:int, edges: List[List[int]]) -> List[int]:
    dist: List[int] = [INF] * (N  + 1)

    def bellman_ford(start: int):
        dist[start] = 0

        for turn in range(N):
            for edge in edges:
                now, dest, cost = edge

                if dist[now] != INF and dist[dest] > dist[now] + cost:
                    dist[dest] = dist[now] + cost

                    if turn == N - 1:
                        return False

        return True

    is_cycle: bool = bellman_ford(1)

    if not is_cycle:
        return [-1]

    for ind in range(2, N + 1):
        if dist[ind] == INF:
            dist[ind] = -1

    return dist[2:]


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    edges: List[List[int]] = []

    for _ in range(M):
        edges.append(list(map(int, input().split())))

    answer: List[int] = solution(N, M, edges)
    for num in answer:
        print(num)