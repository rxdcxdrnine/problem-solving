# leetcode 46

import itertools

def permute_0(nums):
    graph = {}

    for i, num in enumerate(nums):
        graph[num] = nums[:i] + nums[i + 1:]

    length = len(nums)
    result = []

    def recursive_dfs(v, depth, discovered):
        depth += 1
        discovered.append(v)

        if depth == length:
            result.append(discovered)
        else:
            for w in graph[v]:
                if w not in discovered:
                    discovered = recursive_dfs(w, depth, discovered)
                    discovered.pop()

        return discovered[:]

    for num in nums:
        recursive_dfs(num, 0, [])

    return result


def permute_A(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            prev_elements.append(e)

            next_elements = elements[:]
            next_elements.remove(e)
            dfs(next_elements)

            prev_elements.pop()

    dfs(nums)
    return results


def permute_B(nums):
    return list(itertools.permutations(nums))


if __name__ == "__main__":
    print(permute_A([1, 2, 3]))
