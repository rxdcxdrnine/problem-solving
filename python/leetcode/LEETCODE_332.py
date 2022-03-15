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

    dfs(graph, index, visited, route, result, "JFK", 0, len(tickets))
    return result[0]


def dfs(graph: Dict[str, List[str]], index: Dict[str, int], visited: List[List[int]],
        route: List[str], result: List[List[str]], now: str, count: int, target: int):

    if count == target:
        result.append(route[:])
        return

    for dest in graph[now]:
        if len(result) == 1 or visited[index[now]][index[dest]] == 0:
            continue

        visited[index[now]][index[dest]] -= 1
        route.append(dest)

        dfs(graph, index, visited, route, result, dest, count + 1, target)

        visited[index[now]][index[dest]] += 1
        route.pop()


if __name__ == "__main__":
    print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
