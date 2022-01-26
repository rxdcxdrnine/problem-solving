package hackerrank;

import java.io.*;

public class HACKERRANK_time_conversion {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = bufferedReader.readLine();

        String result = timeConversion(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }

    public static String timeConversion(String s) {
        String format = s.substring(s.length() - 2);
        String[] times = s.substring(0, s.length() - 2).split(":");

        int hour = Integer.parseInt(times[0]);
        hour = hour >= 12 ? hour - 12 : hour;
        hour += format.equals("AM") ? 0 : 12;

        return String.format("%02d", hour) + ":" + times[1] + ":" + times[2];
    }
}
