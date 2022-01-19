package programmers;

import java.util.Arrays;
import java.util.PriorityQueue;

public class PROMGRAMMERS_42748 {

    public static void main(String[] args) {
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        System.out.println(Arrays.toString(solution(array, commands)));
    }

    public static int[] solution(int[] array, int[][] commands) {
        int[] answers = new int[commands.length];

        for (int ind = 0; ind < commands.length; ind++) {
            int start = commands[ind][0];
            int end = commands[ind][1];
            int place = commands[ind][2];

            int[] split = Arrays.copyOfRange(array, start - 1, end);

            PriorityQueue<Integer> minHeap = new PriorityQueue<>();

            for (int element: split) {
                minHeap.add(element);
            }

            for (int i = 0; i < (place - 1); i++) {
                minHeap.poll();
            }
            answers[ind] = minHeap.poll();
        }
        return answers;
    }
}
