from typing import List


def letterCombinations(digits: str) -> List[str]:

    if not digits:
        return []

    num_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    graph = {}
    for i in range(len(digits) - 1):
        for letter in num_letters[digits[i]]:
            node = letter + str(i)
            graph[node] = [letter + str(i + 1) for letter in num_letters[digits[i + 1]]]

    stack = []
    combs = []

    for start in list(num_letters[digits[0]]):
        node = start + str(0)
        stack.append({"node": node, "comb": node[0]})

        while stack:
            now = stack.pop()
            if now["node"] in graph:
                for dest in graph[now["node"]]:
                    stack.append({"node": dest, "comb": now["comb"] + dest[0]})
            else:
                combs.append(now["comb"])

    return combs


if __name__ == "__main__":
    digits = "234"
    print(letterCombinations(digits))