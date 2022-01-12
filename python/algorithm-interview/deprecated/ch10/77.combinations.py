# leetcode 77

import itertools

def combine_0(n, k):
    nums = list(range(1, n + 1))

    graph = {}
    for i, num in enumerate(nums):
        graph[num] = nums[i + 1:]

    result = []
    def recursive_dfs(v, depth, discovered):
        discovered.append(v)
        depth += 1

        if depth == k:
            result.append(discovered[:])
        else:
            for w in graph[v]:
                if w not in discovered:
                    discovered = recursive_dfs(w, depth, discovered)
                    discovered.pop()

        return discovered[:]

    for num in nums:
        recursive_dfs(num, 0, [])

    return result


def combine_A(n, k):
    results= []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


def combine_B(n, k):
    return list(itertools.combinations(range(1, n + 1), k))


if __name__ == "__main__":
    print(combine_0(4, 2))
