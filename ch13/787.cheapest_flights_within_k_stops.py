# leetcode 787

import collections
import heapq

def findCheapestPrice_A(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append([v, w])

    k = 0
    Q = [(0, src, k)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price

        if k <= K:
            k += 1
            for v, w in graph[u]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k))

    return -1


if __name__ == "__main__":
    print(findCheapestPrice_A(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))