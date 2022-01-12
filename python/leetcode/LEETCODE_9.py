class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        left, right = 0, 0
        s: str = str(x)
        
        if len(s) % 2 != 0:
            left, right = len(s) // 2, len(s) // 2
        else:
            left, right = len(s) // 2 - 1, len(s) // 2
            
        while left >= 0 and right < len(s):
            
            if s[left] != s[right]:
                return False
            
            left -= 1
            right += 1
            
            
        return True
