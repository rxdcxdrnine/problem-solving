import collections
from typing import List


class Solution:
    # time limit exceeded
    def findMinHeightTrees_0(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph = collections.defaultdict(list)
        for depart, arrive in edges:
            graph[depart].append(arrive)
            graph[arrive].append(depart)

        min_depth = None
        depths = [None for _ in range(n)]
        for node in graph:

            stack = [[node, 0]]  # [node, depth]
            visited = [False for _ in range(n)]
            while stack:

                now = stack.pop()
                visited[now[0]] = True
                depth = now[1] + 1

                if depths[node] is None or depth > depths[node]:
                    depths[node] = depth

                if min_depth is not None and min_depth < depth:
                    continue

                for dest in graph[now[0]]:
                    if not visited[dest]:
                        stack.append([dest, depth])

            if min_depth is None or min_depth > depths[node]:
                min_depth = depths[node]

        result = []
        min_depth = min(depths)
        for ind, depth in enumerate(depths):
            if depth == min_depth:
                result.append(ind)

        return result


    def findMinHeightTrees_1(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for depart, arrive in edges:
            graph[depart] = arrive
            graph[arrive] = depart

        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves



