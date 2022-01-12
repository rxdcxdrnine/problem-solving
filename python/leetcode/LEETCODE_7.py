class Solution:
    def reverse(self, x: int) -> int:
        rev: int = 0
        bound: float = math.pow(2, 31)
            
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(x)[1:][::-1])            
        
        if rev < -bound or rev >= bound:
            return 0
        else:
            return rev
