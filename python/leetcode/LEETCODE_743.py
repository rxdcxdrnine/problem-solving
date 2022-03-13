import collections
from typing import List, Dict, Deque


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph: Dict[int, List[List[int]]] = collections.defaultdict(list)

    for time in times:
        start, end, cost = time
        graph[start].append([end, cost])

    costs: Dict[int, int] = collections.defaultdict(int)
    visited: List[bool] = [False for _ in range(n + 1)]

    costs[k] = 0
    visited[k] = True

    queue: Deque = collections.deque()
    queue.append([k, 0])    # [node, cost]

    while queue:
        now, total = queue.pop()

        for dest, cost in graph[now]:
            if visited[dest] and total + cost >= costs[dest]:
                continue

            costs[dest] = total + cost
            visited[dest] = True
            queue.append([dest, costs[dest]])

    if len(costs) != n:
        return -1

    return max(costs.values())


if __name__ == "__main__":
    print(networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
