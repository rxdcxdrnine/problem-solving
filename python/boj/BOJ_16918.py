from typing import List


def solution(R: int, C:int, N: int, lines: List[str]):
    grid: List[List[int]] = []

    for string in lines:
        line: List[int] = []

        for char in string:
            line.append(3 if char == "O" else 0)

        grid.append(line)

    # 1초 경과
    def time_out(r: int, c:int):
        if grid[r][c] <= 0:
            return

        grid[r][c] -= 1

    # 짝수 초에 설치 -> 남은 시간 3으로 할당
    def set_on(r: int, c: int, n: int):
        if n % 2 != 0 or grid[r][c] != 0:
            return

        grid[r][c] = 3

    # 홀수 초에 폭발 -> 남은 시간 -1 로 할당
    def set_off(r: int, c: int, n: int):
        if n <= 1 or n % 2 != 1 or grid[r][c] != 0:
            return

        grid[r][c] = -1

        if 0 <= r - 1:
            grid[r - 1][c] = -1

        if 0 <= c - 1:
            grid[r][c - 1] = -1

        # 오른쪽/아래쪽의 원소가 남은 시간이 1이면 건너뛰기
        if r + 1 < R and grid[r + 1][c] != 1:
            grid[r + 1][c] = -1

        if c + 1 < C and grid[r][c + 1] != 1:
            grid[r][c + 1] = -1

    # 폭발 후에 초기화 -> 남은 시간 0 으로 할당
    def set_init(n: int):
        for r in range(R):
            for c in range(C):
                if n % 2 != 1 or grid[r][c] != -1:
                    continue

                grid[r][c] = 0

    # 순회
    for n in range(1, N + 1):
        for r in range(R):
            for c in range(C):
                time_out(r, c)
                set_on(r, c, n)
                set_off(r, c, n)

        set_init(n)

    # 출력
    for line in grid:
        string: str = ""

        for num in line:
            string += "." if num == 0 else "O"

        print(string)


if __name__ == "__main__":
    R, C, N = list(map(int, input().split()))
    lines: List[str] = []

    for _ in range(R):
        lines.append(input())

    solution(R, C, N, lines)
