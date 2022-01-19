package leetcode;

import java.util.Arrays;
import java.util.Comparator;

class LEETCODE_14 {
    public String longestCommonPrefix(String[] strs) {

        String prefix = "";
        String shortest = Arrays.stream(strs)
            .min(Comparator.comparing(String::length))
            .get();
        
        int ind = 0;
        
        while (ind < shortest.length()) {
            
            for (String s : strs) {
                if (shortest.charAt(ind) != s.charAt(ind))
                    return prefix;
            }
            
            prefix += shortest.charAt(ind);
            ind++;
        }
        
        return prefix;
    }
}
