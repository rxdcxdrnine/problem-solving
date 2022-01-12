import collections
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    nodes = []

    for depart, arrive in prerequisites:
        nodes.append(depart)
        graph[depart].append(arrive)

    stack = []

    for node in nodes:
        stack.append({"node": node, "course": [node]})

        while stack:
            now = stack.pop()

            if graph[now["node"]]:

                filters = []
                for index, dest in enumerate(graph[now["node"]]):
                    filters.append(index)
                    if dest in now["course"]:
                        return False
                    else:
                        stack.append({"node": dest, "course": now["course"] + [dest]})

                graph[now["node"]] = [dest for index, dest in enumerate(graph[now["node"]]) \
                                      if index not in filters]

    return True


if __name__ == "__main__":
    numCourses, prerequisites = 3, [[0, 1], [0, 2], [1, 2]]
    print(canFinish(numCourses, prerequisites))
