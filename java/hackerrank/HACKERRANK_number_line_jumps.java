package hackerrank;

import java.io.*;

public class HACKERRANK_number_line_jumps {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int x1 = Integer.parseInt(firstMultipleInput[0]);

        int v1 = Integer.parseInt(firstMultipleInput[1]);

        int x2 = Integer.parseInt(firstMultipleInput[2]);

        int v2 = Integer.parseInt(firstMultipleInput[3]);

        String result = kangaroo(x1, v1, x2, v2);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }

    public static String kangaroo(int x1, int v1, int x2, int v2) {

        if (v1 == v2)
            return x1 == x2 ? "YES" : "NO";

        double t = - (x1 - x2) / (double) (v1 - v2);

        if (t < 0)
            return "NO";
        else
            return t == (int) t ? "YES" : "NO";
    }

}
