package leetcode;

class LEETCODE_9 {
    public boolean isPalindrome(int x) {
        
        if (x < 0)
            return false;
        
        int left, right;
        String s = Integer.toString(x);
            
        if (s.length() % 2 != 0) {
            left = s.length() / 2;
            right = s.length() / 2;
        } else {
            left = s.length() / 2 - 1;
            right = s.length() / 2;
        }
        
        while (left >= 0 && right < s.length()) {
            
            if (s.charAt(left--) != s.charAt(right++)) {
                return false;
            }
        }
        
        return true;
    }
}
