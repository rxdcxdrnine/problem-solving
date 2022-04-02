package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PROGRAMMERS_42840 {

    public static void main(String[] args) {
        int[] answers = {1, 3, 2, 4, 2};

        System.out.println(Arrays.toString(solution(answers)));

    }

    public static int[] solution(int[] answers) {
        int NUM_STUDENT = 3;

        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int[] result = {0, 0, 0};

        for (int ind = 0; ind < answers.length; ind++) {
            if (answers[ind] == first[ind % first.length]) {
                result[0] += 1;
            }
            if (answers[ind] == second[ind % second.length]) {
                result[1] += 1;
            }
            if (answers[ind] == third[ind % third.length]) {
                result[2] += 1;
            }
        }

        int maxVal = Arrays.stream(result).max().getAsInt();
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < NUM_STUDENT; i++) {
            if (result[i] == maxVal) {
                answer.add(i + 1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
