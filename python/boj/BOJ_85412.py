from typing import List, Union


class Reference:

    def __init__(self, val: Union[int, bool]):
        self.val = val


def solution(word: str) -> int:
    chars: List[str] = ["A", "E", "I", "O", "U"]
    route: List[str] = []

    count: Reference = Reference(0)
    check: Reference = Reference(False)

    def dfs():
        if len(route) > 5 or check.val:
            return

        if len(route) >= 1:
            count.val += 1

        for char in chars:
            route.append(char)

            if "".join(route) == word:
                count.val += 1
                check.val = True

            dfs()
            route.pop()

    dfs()
    return count.val


if __name__ == "__main__":
    print(solution("EIO"))
