class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix: str = ""
        short: str = min(strs, key=lambda x: len(x))
        ind: int = 0
            
        while ind < len(short):
            
            for s in strs:
                if short[ind] != s[ind]:
                    return prefix
                
            prefix += short[ind]
            ind += 1
            
        return prefix
