from typing import List


def solution(plane: List[List[int]], point: List[int]):
    num_row: int = len(plane)
    num_col: int = len(plane[0])
    answer: int = 0

    while True:
        row, col, drc = point[0], point[1], point[2]

        if plane[row][col] != 2:
            plane[row][col] = 2
            answer += 1
        count: int = 0

        while True:
            row, col = point[0], point[1]
            if count == 4:
                break

            if drc == 0:
                col -= 1
            if drc == 1:
                row -= 1
            if drc == 2:
                col += 1
            if drc == 3:
                row += 1

            drc = (drc - 1) % 4

            if 0 <= row < num_row and 0 <= col < num_col and plane[row][col] == 0:
                point[0], point[1], point[2] = row, col, drc
                break

            count += 1

        if count == 4:
            row, col, drc = point[0], point[1], point[2]

            if drc == 0:
                row += 1
            if drc == 1:
                col -= 1
            if drc == 2:
                row -= 1
            if drc == 3:
                col += 1

            if 0 <= row < num_row and 0 <= col < num_col:
                if plane[row][col] != 1:
                    point[0], point[1], point[2] = row, col, drc
                else:
                    break

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    point: List[int] = [r, c, d]

    plane: List[List[int]] = []
    for _ in range(N):
        plane.append(list(map(int, input().split())))

    print(solution(plane, point))
