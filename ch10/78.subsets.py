# leetcode 78

def subsets_0(nums):
    graph = {}
    graph['*'] = ['*'] + nums

    for i, num in enumerate(nums):
        graph[num] = nums[i + 1:]

    result = []
    def recursive_dfs(v, depth=0, discovered=[]):
        discovered.append(v)
        depth += 1

        if depth == len(nums):
            result.append(discovered)
        else:
            for w in graph[v]:
                discovered = recursive_dfs(w, depth, discovered)
                discovered.pop()

        return discovered[:]

    for key in graph.keys():
        recursive_dfs(key, 0, [])

    result = [list(filter(lambda x: x != '*', element)) for element in result]
    return result


def subset_A(nums):
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result



if __name__ == "__main__":
    print(subsets([1, 2, 3, 4]))