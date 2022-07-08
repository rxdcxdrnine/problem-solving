from typing import List


def solution(places):
    result: List[int] = []

    def is_distancing(place: List[List[int]]):
        rows: int = len(place)
        cols: int = len(place[0])

        for r in range(rows):
            for c in range(cols):

                if place[r][c] != "P":
                    continue

                if r + 1 < rows and place[r + 1][c] == "P":
                    return 0

                if c + 1 < cols and place[r][c + 1] == "P":
                    return 0

                if r - 1 >= 0 and place[r - 1][c] == "P":
                    return 0

                if r + 2 < rows and place[r + 2][c] == "P" and place[r + 1][c] != "X":
                    return 0

                if c + 2 < cols and place[r][c + 2] == "P" and place[r][c + 1] != "X":
                    return 0

                if r - 2 >= 0 and place[r - 2][c] == "P" and place[r - 1][c] != "X":
                    return 0

                if r + 1 < rows and c + 1 < cols and place[r + 1][c + 1] == "P" and \
                        (place[r + 1][c] != "X" or place[r][c + 1] != "X"):
                    return 0

                if r - 1 >= 0 and c + 1 < cols and place[r - 1][c + 1] == "P" and \
                        (place[r - 1][c] != "X" or place[r][c + 1] != "X"):
                    return 0

        return 1

    for place in places:
        result.append(is_distancing(place))

    return result


if __name__ == "__main__":
    print(solution(
        [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    ))
