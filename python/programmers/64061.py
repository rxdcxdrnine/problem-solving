from typing import List

def solution(board, moves):
    answer: int = 0
    stack: List[int] = []

    transposed: List[List[int]] = []
    rows: int = len(board)
    cols: int = len(board[0])

    for col in range(cols):
        transposed.append([0] * rows)

    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = board[row][col]

    for move in moves:
        depth: int = len(transposed[move - 1]) - 1

        while len(transposed[move - 1]) > 0:

            if transposed[move - 1][0] != 0:
                last: int = transposed[move - 1].pop(0)

                if stack and last == stack[-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(last)
                break

            else:
                transposed[move - 1].pop(0)

            depth -= 1

    return answer


if __name__ == "__main__":
    board: List[List[int]] = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves: List[int] = [1,5,3,5,1,2,1,4]

    print(solution(board, moves))