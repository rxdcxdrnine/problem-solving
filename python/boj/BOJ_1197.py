from typing import List, Tuple


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a: int = find_parent(parent, a)
    b: int = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(V: int, edges: List[Tuple[int, int, int]]):
    parent: List[int] = [0] * (V + 1)
    for ind in range(1, V + 1):
        parent[ind] = ind

    edges.sort()

    result: int = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result


if __name__ == "__main__":
    V, E = map(int, input().split())
    edges: List[Tuple[int, int, int]] = []

    for _ in range(E):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    print(solution(V, edges))
