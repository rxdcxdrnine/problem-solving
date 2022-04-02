import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

// https://www.acmicpc.net/problem/1052
public class BOJ_1052 {
    private static final String SMALL = "small";
    private static final String LARGE = "large";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] strs = br.readLine().split(" ");
        int N = Integer.parseInt(strs[0]);
        int K = Integer.parseInt(strs[1]);

        int result = recursion(N, K);
        bw.write(Integer.toString(result));

        br.close();
        bw.close();
    }

    private static int recursion(int N, int K) {
        if (N <= K) {
            return 0;
        }
        if (K == 1) {
            int square = getNearestSqaure(N, LARGE);
            return square - N;
        } else {
            int square = getNearestSqaure(N, SMALL);
            return recursion(square, 1) + recursion(N - square, K - 1);
        }
    }

    private static int getNearestSqaure(int n, String compare) {
        int m = 1;
        if (compare == SMALL) {
            while (n >= m * 2) {
                m *= 2;
            }
        }
        if (compare == LARGE) {
            while (n > m) {
                m *= 2;
            }
        }
        return m;
    }
}