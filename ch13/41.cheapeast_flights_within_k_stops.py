import collections
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

    graph = collections.defaultdict(list)
    node_price = {i: None for i in range(n)}

    for depart, arrive, price in flights:
        graph[depart].append([arrive, price])

    min_price = None
    queue = collections.deque([[src, 0, 0]])  # [node, cum_price, cum_distance]

    while queue:
        now = queue.popleft()

        for dest in graph[now[0]]:
            cum_price = now[1] + dest[1]
            cum_distance = now[2] + 1
            if cum_distance - 1 <= k:
                if dest[0] == dst:
                    if min_price is None or min_price > cum_price:
                        min_price = cum_price
                else:
                    if node_price[dest[0]] is None or node_price[dest[0]] > cum_price:
                        node_price[dest[0]] = cum_price
                        queue.append([dest[0], cum_price, cum_distance])

    return min_price if min_price is not None else -1


if __name__ == "__main__":
    n, flights, src, dst, k = 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
    print(findCheapestPrice(n, flights, src, dst, k))
