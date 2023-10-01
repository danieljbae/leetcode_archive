class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Analysis:
        Time: O(n log n)
        Space: O(1)
        """
        if len(s) != len(t):
            return False 
        
        s = sorted(s)
        t = sorted(t)
        
        for c1,c2 in zip(s,t):
            if c1 != c2:
                return False
        return True
        