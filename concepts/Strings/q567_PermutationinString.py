from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        def isPerm(s1,s2):
            return collections.Counter(s1) == collections.Counter(s2)
        
        beg, end = 0, len(s1)-1
        while end < len(s2):
            windowStr = s2[beg:end+1]
            if isPerm(s1,windowStr):
                return True
            else:
                beg += 1
                end += 1
        return False
                
                
                
        
        
        
        
        