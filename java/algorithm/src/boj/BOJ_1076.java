import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BOJ_1076 {

    static final Map<String, long[]> colorMap = new HashMap<>() {
        {
            put("black", new long[] { 0, 1 });
            put("brown", new long[] { 1, 10 });
            put("red", new long[] { 2, 100 });
            put("orange", new long[] { 3, 1_000 });
            put("yellow", new long[] { 4, 10_000 });
            put("green", new long[] { 5, 100_000 });
            put("blue", new long[] { 6, 1_000_000 });
            put("violet", new long[] { 7, 10_000_000 });
            put("grey", new long[] { 8, 100_000_000 });
            put("white", new long[] { 9, 1_000_000_000 });
        }
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String buf;
        List<String> colors = new ArrayList<>();

        while ((buf = br.readLine()) != null) {
            colors.add(buf);
        }

        bw.write((Long.toString(calculate(colors))));

        br.close();
        bw.close();
    }

    static long calculate(List<String> colors) throws IllegalArgumentException {
        if (colors.size() != 3) {
            throw new IllegalArgumentException();
        }

        long first = colorMap.get(colors.get(0))[0];
        long second = colorMap.get(colors.get(1))[0];
        long third = colorMap.get(colors.get(2))[1];

        return ((first * 10) + second) * third;
    }
}
