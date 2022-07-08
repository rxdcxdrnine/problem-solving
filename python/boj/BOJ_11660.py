from typing import List

def solution(sum_table: List[List[int]], case: List[int]) -> int:
    x1, y1, x2, y2 = case
    total: int = 0

    for x in range(x1 - 1, x2):
        total += sum_table[x][y2 - 1] - (sum_table[x][y1 - 2] if y1 > 1 else 0)

    return total


def prefix_sum(table: List[List[int]]) -> List[List[int]]:
    sum_table: List[List[int]] = []

    for row in table:
        sum_list: List[int] = []

        tmp: int = 0
        for ind in range(len(row)):
            tmp += row[ind]
            sum_list.append(tmp)

        sum_table.append(sum_list)

    return sum_table


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    table: List[List[int]] = []
    cases: List[List[int]] = []

    for _ in range(N):
        table.append(list(map(int, input().split())))

    for _ in range(M):
        cases.append(list(map(int, input().split())))

    sum_table: List[List[int]] = prefix_sum(table)

    for case in cases:
        print(solution(sum_table, case))
