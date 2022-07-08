from typing import List


def solution(n: int, m: int, r: int, arr: List[List[int]]) -> List[List[int]]:
    def rotate():
        check: int = min(n, m) // 2

        for cnt in range(check):
            n_max, m_max = n - cnt - 1, m - cnt - 1
            tmp: int = arr[cnt][cnt]

            # 위쪽 변
            for i in range(cnt, m_max):
                arr[cnt][i] = arr[cnt][i + 1]

            # 오른쪽 변
            for i in range(cnt, n_max):
                arr[i][m_max] = arr[i + 1][m_max]

            # 아래쪽 변
            for i in range(m_max, cnt, -1):
                arr[n_max][i] = arr[n_max][i - 1]

            # 왼쪽 변
            for i in range(n_max, cnt, -1):
                arr[i][cnt] = arr[i - 1][cnt]

            arr[cnt + 1][cnt] = tmp

    for _ in range(r):
        rotate()

    return arr


if __name__ == "__main__":
    N, M, R = map(int, input().split())
    arr: List[List[int]] = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    answer: List[List[int]] = solution(N, M, R, arr)

    for row in answer:
        print(" ".join([str(num) for num in row]))

