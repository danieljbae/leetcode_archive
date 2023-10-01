class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int

        Warm up for "424. Longest Repeating Character Replacement"

        Analysis: 
        - Time: O(n) 
        - Space: O(1) w.c. as anchor is at most size of 1
        """
        n = len(s)
        
        # Base case
        if not s:
            return 0
        
        
        globalMax = localMax = 1
        anchor = ''
        
        for i,char in enumerate(s):
            
            if char == anchor:
                localMax += 1
                globalMax = max(localMax,globalMax)
            else:
                localMax = 1
                anchor = char # reset anchor / left most char

        return globalMax