from typing import List


def find_parent(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent: List[int], a: int, b: int) -> None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(v: int, edges: List[List[int]]) -> int:
    parent = [0 for _ in range(v + 1)]
    for ind in range(1, v + 1):
        parent[ind] = ind

    result: int = 0
    num_edges: int = 0

    # edges: [[start, end, cost]]
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            num_edges += 1

        if num_edges == v - 2:
            break

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges: List[List[int]] = []

    for _ in range(M):
        edges.append(list(map(int, input().split())))

    print(solution(N, edges))
