from typing import List, Tuple


def solution(cases: List[Tuple[int, List[int]]]) -> List[List[List[int]]]:
    answers: List[List[List]] = []

    for case in cases:
        k, nums = case

        visited: List[bool] = [False for _ in range(len(nums))]
        route: List[int] = []
        result: List[List[int]] = []

        def dfs(now: int):
            if len(route) == 6:
                result.append(route[:])

            for ind in range(now + 1, len(nums)):
                if visited[ind]:
                    continue

                visited[ind] = True
                route.append(nums[ind])
                dfs(ind)

                visited[ind] = False
                route.pop()

        dfs(-1)
        answers.append(result)

    return answers


if __name__ == "__main__":
    cases: List[Tuple[int, List[int]]] = []

    while True:
        line: str = input()

        if line == "0":
            break

        arr: List[int] = list(map(int, line.split()))
        cases.append((arr[0], arr[1:]))

    answers: List[List[List[int]]] = solution(cases)

    for answer in answers:
        for nums in answer:
            print(' '.join(list(map(str, nums))))
        print()
