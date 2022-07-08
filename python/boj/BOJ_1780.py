from typing import List


def solution(arr: List[List[int]]) -> List[int]:
    view: List[int] = []
    for row in arr:
        view.extend(row)

    if list(set(view)) == [-1]:
        return [1, 0, 0]
    if list(set(view)) == [0]:
        return [0, 1, 0]
    if list(set(view)) == [1]:
        return [0, 0, 1]

    size: int = len(arr) // 3

    nw: List[List[int]] = [arr[i][:size] for i in range(0, size)]
    n: List[List[int]] = [arr[i][size: size * 2] for i in range(0, size)]
    ne: List[List[int]] = [arr[i][size * 2:] for i in range(0, size)]

    w: List[List[int]] = [arr[i][:size] for i in range(size, size * 2)]
    c: List[List[int]] = [arr[i][size:size * 2] for i in range(size, size * 2)]
    e: List[List[int]] = [arr[i][size * 2:] for i in range(size, size * 2)]

    sw: List[List[int]] = [arr[i][:size] for i in range(size * 2, size * 3)]
    s: List[List[int]] = [arr[i][size:size * 2] for i in range(size * 2, size * 3)]
    se: List[List[int]] = [arr[i][size * 2:] for i in range(size * 2, size * 3)]

    nw: List[int] = solution(nw)
    n: List[int] = solution(n)
    ne: List[int] = solution(ne)

    w: List[int] = solution(w)
    c: List[int] = solution(c)
    e: List[int] = solution(e)

    sw: List[int] = solution(sw)
    s: List[int] = solution(s)
    se: List[int] = solution(se)

    result = [0, 0, 0]
    for frac in [nw, n, ne, w, c, e, sw, s, se]:
        result[0] += frac[0]
        result[1] += frac[1]
        result[2] += frac[2]

    return result


if __name__ == "__main__":
    N: int = int(input())

    arr: List[List[int]] = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    answer: List[int] = solution(arr)
    for num in answer:
        print(num)
