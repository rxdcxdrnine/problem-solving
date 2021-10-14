from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

    graph = {nums[i]: nums[i + 1:] for i in range(len(nums))}

    subsets = [[]]
    stack = []

    for num in nums:
        stack.append({"node": num, "subset": [num]})

        while stack:
            now = stack.pop()
            subsets.append(now["subset"])

            for dest in graph[now["node"]]:
                if dest not in now["subset"]:
                    stack.append({"node": dest, "subset": now["subset"] + [dest]})

    return subsets


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))