# leetcode 207

import collections

# time limit exceeded
def canFinish_0(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for after, before in prerequisites:
        graph[before].append(after)

    default = True
    def recursive_dfs(v, result, discovered):
        if v in discovered:
            discovered.append(v)
            result = False
        else:
            discovered.append(v)
            for w in graph[v]:
                if not result:
                    break
                discovered, result = recursive_dfs(w, result, discovered)
                discovered.pop()

        return discovered[:], result

    for key in graph.keys():
        _, default = recursive_dfs(key, default, [])

    return default


def canFinish_A(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    def dfs(i):
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True


if __name__ == "__main__":
    print(canFinish_A(2, [[2, 1], [1, 0]]))