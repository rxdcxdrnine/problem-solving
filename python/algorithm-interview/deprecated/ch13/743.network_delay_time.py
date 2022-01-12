# leetcode 743

import collections
import heapq

def networkDelayTime_A(times, n, k):
    graph = collections.defaultdict(int)
    for u, v, w in times:
        graph[u].append((v, w))

    Q = [(0, k)]
    dist = collections.defaultdict(int)

    while Q:

        # 1. 최소 힙에서 heappop
        time, node = heapq.heappop(Q)

        ## 2-1. 추출한 노드를 처음 방문한 경우, dist 에 기록
        ## 2-2. 추출한 노드를 이미 방문한 경우, dist 에 기록 불가
        ## ㄴ 이후 삽입된 경로는 이미 앞에서 해당 노드에 도달하기도 전에,
        ##   이전 삽입된 경로에 의해 우선순위에 밀려있었으므로 반드시 이전 삽입된 경로보다 소요시간이 더 김
        if node not in dist:
            dist[node] = time

            ## 3. 인접노드까지 소요시간 계산 후 heappush
            ## ㄴ 만약 dist[v] 가 alt 보다 작을 경우, 이미 dist[v] 가 기록이 되어있으므로 alt 는 dist[v] 에 기록 불가
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    ## 다익스트라 알고리즘 구현 시 2가지 고려
    ## 1. 모든 노드가 신호를 받는데 걸리는 시간
    ## 2. 모든 노드에 도달할 수 있는지 여부 -> 아래에서 체크
    if len(dist) == n:
        return max(dist.values())

    return -1


if __name__ == "__main__":
    networkDelayTime_A([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)