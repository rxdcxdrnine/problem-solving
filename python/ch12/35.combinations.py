from typing import List


def combine(n: int, k: int) -> List[List[int]]:

    nums = [i for i in range(1, n + 1)]
    graph = {nums[i]: nums[i + 1:] for i in range(len(nums))}

    combs = []
    stack = []

    for num in nums:
        stack.append({"node": num, "comb": [num]})

        while stack:
            current = stack.pop()

            if len(current["comb"]) == k:
                combs.append(current["comb"])

            for dest in graph[current["node"]]:
                stack.append({"node": dest, "comb": current["comb"] + [dest]})

    return combs


if __name__ == "__main__":
    n, k = 5, 4
    print(combine(n, k))
