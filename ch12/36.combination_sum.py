from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    graph = {}
    for i in range(len(candidates)):
        graph[candidates[i]] = candidates[i:]

    stack = []
    combs = []

    for num in candidates:
        stack.append({"node": num, "comb": [num]})

        while stack:
            now = stack.pop()

            if sum(now["comb"]) == target:
                combs.append(now["comb"])
            else:
                for dest in graph[now["node"]]:
                    if sum(now["comb"]) + dest <= target:
                        stack.append({
                            "node": dest,
                            "comb": now["comb"] + [dest]
                        })

    return combs


if __name__ == "__main__":
    candidates, target = [2, 3, 5], 8
    print(combinationSum(candidates, target))
