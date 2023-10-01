class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Analysis:
        Time: O(n)
        Space: O(1) table array is fixed
        """
        # base 
        if len(s) != len(t):
            return False
        
        n = len(s)
        table = [0]*26
        
        # increase
        for i in range(n):
            table[ord(s[i]) - ord('a')] += 1
        
        # decrease
        for i in range(n):
            table[ord(t[i]) - ord('a')] -= 1
            if table[ord(t[i]) - ord('a')] < 0: # validate
                return False
        
        return True
         
        