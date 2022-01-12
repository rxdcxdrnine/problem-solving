class Solution {
    public String longestCommonPrefix(String[] strs) {

        String prefix = "";
        String shortest = Arrays.asList(strs).stream()
            .min(Comparator.comparing(x -> x.length()))
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
