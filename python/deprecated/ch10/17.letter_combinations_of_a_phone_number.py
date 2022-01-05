# leetcode 17


def letterCombinations_0(digits):
    graph = {}
    numbers = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

    for i in range(len(digits) - 1):
        for char in numbers[digits[i]]:
            graph[char + str(i)] = list(map(lambda x: x + str(i + 1), list(numbers[digits[i + 1]])))


    if len(digits) > 0:
        first = numbers[digits[0]]
    else:
        return []

    combinations = []
    def recursive_dfs(v, discovered=[]):
        discovered.append(v)
        if graph.get(v) is None:
            combinations.append(''.join(discovered)[::2])
        else:
            for w in graph[v]:
                discovered = recursive_dfs(w, discovered)
                discovered.remove(w)
        return discovered

    for char in first:
        char += '0'
        recursive_dfs(char, [])

    return combinations


def letterCombinations_A(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    if not digits:
        return []

    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    dfs(0, '')

    return result


if __name__ == "__main__":
    print(letterCombinations_0('234'))