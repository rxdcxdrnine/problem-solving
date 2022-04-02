package leetcode;

class LEETCODE_7 {
    public int reverse(int x) {
        long rev = 0;
        double bound = Math.pow(2, 31);
        
        boolean isNegative = x < 0;
        long num = Math.abs((long) x);
        
        while (num >= 10) {
            long mod = num % (long) 10;
            num = num / (long) 10;
            rev = 10 * rev + mod;
        }
        rev = 10 * rev + num;
        
        if (rev < -bound || rev >= bound) {
            return 0;
        } else if (isNegative) {
            return (int)-rev;
        } else {
            return (int) rev;
        }
    }
}
