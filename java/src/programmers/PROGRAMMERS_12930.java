package programmers;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PROGRAMMERS_12930 {

    public static void main(String[] args) {

        String s = " try  hello  world ";
        System.out.println(solution(s));
    }

    public static String solution(String s) {
        StringBuilder sb = new StringBuilder();

        Pattern pat = Pattern.compile("(\\w+)|(\\s+)");
        Matcher match = pat.matcher(s);

        while (match.find()) {
            String token = match.group();
            StringBuilder str = new StringBuilder();

            for (int ind = 0; ind < token.length(); ind++) {
                char c = token.charAt(ind);

                if (ind % 2 == 0 && 'a' <= c && c <= 'z') {
                    c = (char) (c - 'a' + 'A');
                }
                if (ind % 2 == 1 && 'A' <= c && c <= 'Z') {
                    c = (char) (c - 'A' + 'a');
                }
                str.append(c);
            }
            sb.append(str);
        }
        return sb.toString();
    }

}
