class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        Analysis: Double pointer approach
        Time = O(n)
        Space = O(n)
        """
        l, r = 0, len(s)-1
        
        while  l < r:    
            if s[l].isalnum() and s[r].isalnum(): # both valid chars
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            else: # both invalid chars or one is invalid
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
        return True
            
            
        
        