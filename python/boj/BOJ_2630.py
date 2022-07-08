from typing import List


def divide(arr: List[List[int]], n: int) -> List[int]:
    total: int = 0
    for row in arr:
        total += sum(row)

    if total == 0:
        return [1, 0]
    if total == len(arr) ** 2:
        return [0, 1]

    nw: List[List[int]] = [arr[i][:n // 2] for i in range(n // 2)]
    ne: List[List[int]] = [arr[i][n // 2:] for i in range(n // 2)]
    sw: List[List[int]] = [arr[i][:n // 2] for i in range(n // 2, n)]
    se: List[List[int]] = [arr[i][n // 2:] for i in range(n // 2, n)]

    nw: List[int] = divide(nw, n // 2)
    ne: List[int] = divide(ne, n // 2)
    sw: List[int] = divide(sw, n // 2)
    se: List[int] = divide(se, n // 2)

    result = [0, 0]
    for fraction in [nw, ne, sw, se]:
        result[0] += fraction[0]
        result[1] += fraction[1]
    return result


if __name__ == "__main__":
    N: int = int(input())
    arr: List[List[int]] = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    answer: List[int] = divide(arr, N)
    print(answer[0])
    print(answer[1])

