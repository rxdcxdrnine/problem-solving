import collections
from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for depart, arrive in tickets:
        graph[depart].append(arrive)

    for depart in graph:
        graph[depart].sort(reverse=True)

    itinerary = ["JFK"]
    stack = [{"node": "JFK", "itinerary": ["JFK"], "tickets": tickets}]

    while stack:
        now = stack.pop()

        if len(now["itinerary"]) == len(tickets) + 1:
            return now["itinerary"]
        else:
            for dest in graph[now["node"]]:
                if [now["node"], dest] in now["tickets"]:
                    ind = now["tickets"].index([now["node"], dest])
                    stack.append({
                        "node": dest,
                        "itinerary": now["itinerary"] + [dest],
                        "tickets": now["tickets"][:ind] + now["tickets"][ind + 1:]
                    })

    return None
