from typing import List


def permute(nums: List[int]) -> List[List[int]]:

    graph = {}
    for i in range(len(nums)):
        graph[nums[i]] = nums[:i] + nums[i + 1:]

    stack = []
    perms = []

    for num in nums:
        stack.append({"node": num, "perm": [num]})

        while stack:
            current = stack.pop()

            if len(current["perm"]) == len(nums):
                perms.append(current["perm"])

            for dest in graph[current["node"]]:
                if dest not in current["perm"]:
                    stack.append({"node": dest, "perm": current["perm"] + [dest]})

    return perms


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))
