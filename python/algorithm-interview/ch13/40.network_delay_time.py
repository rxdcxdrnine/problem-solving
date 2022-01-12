import collections
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:

    graph = collections.defaultdict(list)
    for depart, arrive, time in times:
        graph[depart].append({"node": arrive, "time": time})

    cum_times = {k: 0}
    queue = collections.deque([{"node": k, "cum_time": 0}])

    while queue:
        now = queue.popleft()

        for dest in graph[now["node"]]:
            node = dest["node"]
            time = dest["time"]
            cum_time = now["cum_time"] + time

            if node not in cum_times or cum_times[node] > cum_time:
                cum_times[node] = cum_time
                queue.append({"node": node, "cum_time": cum_time})

    if len(cum_times) != n:
        return -1
    else:
        max_val = 0
        for val in cum_times.values():
            if max_val < val:
                max_val = val

        return max_val


if __name__ == "__main__":
    times, N, K = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
    print(networkDelayTime(times, N, K))
