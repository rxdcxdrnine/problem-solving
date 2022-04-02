package programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class PROGRAMMERS_64061 {

    public static void main(String[] args) {
        int[][] board = {
            {0, 0, 0, 0, 0},
            {0, 0, 1, 0, 3},
            {0, 2, 5, 0, 1},
            {4, 2, 4, 4, 2},
            {3, 5, 1, 3, 1},
        };
        int[] moves = {1, 5, 3, 5, 1, 2, 1, 4};

        System.out.println(solution(board, moves));
    }

    private static int solution(int[][] board, int[] moves) {

        List<List<Integer>> transposed = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        int answer = 0;

        for (int i = 0; i < board[0].length; i++) {
            transposed.add(
                new ArrayList<>(Collections.nCopies(board.length, 0)));
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                transposed.get(j).set(i, board[i][j]);
            }
        }

        for (int move : moves) {

            while (transposed.get(move - 1).size() > 0) {
                Integer last = transposed.get(move - 1).remove(0);

                if (last != 0) {
                    if (stack.size() > 0 && stack.peek().equals(last)) {
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.push(last);
                    }
                    break;
                }
            }
        }

        return answer;
    }
}
