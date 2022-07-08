import collections
from typing import List, Dict


def solution(orders: List[str], course: List[int]) -> List[str]:

    counts: Dict[str, int] = collections.defaultdict(int)

    def dfs(chars: str, ind: int):

        comb: str = "".join(route)

        if len(comb) > 1:
            counts[comb] += 1

        for ind in range(ind, len(chars)):
            route.append(chars[ind])
            dfs(chars, ind + 1)
            route.pop()

    for order in orders:
        route: List[str] = []
        dfs("".join(sorted(order)), 0)

    answer: List[str] = []
    for num in course:
        max_val: int = 0
        result: List[str] = []

        for comb, count in counts.items():
            if len(comb) != num or count < 2:
                continue

            if count > max_val:
                result = [comb]
            elif count == max_val:
                result.append(comb)

            max_val = max(max_val, count)

        answer.extend(result)

    return sorted(answer)


if __name__ == "__main__":
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
