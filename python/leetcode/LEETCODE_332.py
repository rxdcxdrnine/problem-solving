import collections
from typing import List, Dict, Set


def findItinerary(tickets: List[List[str]]) -> List[str]:

    nodes: Set[str] = set()

    for depart, arrive in tickets:
        nodes.add(depart)
        nodes.add(arrive)

    index: Dict[str, int] = {node: ind for ind, node in enumerate(set(nodes))}
    visited: List[List[int]] = [[0 for _ in nodes] for _ in nodes]
    graph: Dict[str, List[str]] = collections.defaultdict(list)

    for depart, arrive in sorted(tickets):
        graph[depart].append(arrive)
        visited[index[depart]][index[arrive]] += 1

    route: List[str] = ["JFK"]
    result: List[List[str]] = []

    def dfs(now: str, count: int):

        if count == len(tickets):
            result.append(route[:])
            return

        for dest in graph[now]:
            if len(result) == 1 or visited[index[now]][index[dest]] == 0:
                continue

            visited[index[now]][index[dest]] -= 1
            route.append(dest)

            dfs(dest, count + 1)

            visited[index[now]][index[dest]] += 1
            route.pop()

    dfs("JFK", 0)
    return result[0]


if __name__ == "__main__":
    print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
