package boj;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// https://www.acmicpc.net/problem/1009
public class BOJ_1009 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        List<int[]> data = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] strs = br.readLine().split(" ");
            int[] ints = Arrays.stream(strs).mapToInt(Integer::parseInt).toArray();
            data.add(ints);
        }

        for (int i = 0; i < n; i++) {
            int[] ints = data.get(i);
            bw.write(solution(ints[0], ints[1]) + "\n");
        }

        br.close();
        bw.close();
    }

    public static int solution(int a, int b) {
        List<Integer> remains = new ArrayList<>();
        int rest = a % 10;

        for (int i = 0; i < b; i++) {
            remains.add(rest);
            rest = (rest * a) % 10;

            if (remains.contains(rest))
                break;
        }

        int index = b % remains.size() == 0 ? remains.size() - 1 : b % remains.size() - 1;
        int answer = remains.get(index);
        return answer != 0 ? answer : 10;
    }
}