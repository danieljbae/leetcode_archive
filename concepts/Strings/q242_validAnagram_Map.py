class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Analysis:
        Time: O(n)
        Space: O(n) w.c. all chars are unique 
        """
        if len(s) == 0 or len(t) == 0:
            return True
        
        d = {}
        
        # increase
        for c in s:
            if c in d:
                d[c] += 1 
            else:
                d[c] = 1
        
        # decrease
        for c in t: 
            if c in d:
                d[c] -= 1 
            else:
                return False
        
        # validate
        if len(set(d.values())) == 1 and 0 in set(d.values()):
            return True
        
        return False
        