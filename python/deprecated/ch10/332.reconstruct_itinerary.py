# leetcode 332

import collections

def findItinerary_0(tickets):
    graph = collections.defaultdict(list)
    for ticket in sorted(tickets):
        graph[ticket[0]].append(ticket[1])


    result = []
    def recursive_dfs(v, depth, discovered):
        discovered.append(v)
        depth += 1

        if depth == len(tickets) + 1:
            result.append(discovered)
        else:
            if v in graph:
                for w in graph[v][:]:
                    graph[v].remove(w)
                    discovered = recursive_dfs(w, depth, discovered)
                    discovered.pop()
                    graph[v].append(w)
                    
                   if len(result) == 1:
                       break

        return discovered[:]

    recursive_dfs("JFK", 0, [])
    result.sort()

    return result[0]


def findItinerary_A(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs("JFK")
    return route[::-1]


if __name__ == "__main__":
    print(findItinerary_A([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
