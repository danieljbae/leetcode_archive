class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        L_count = 0
        R_count = 0 
        
        bal_count = 0
        
        for el in s:
            if el == "L":
                L_count += 1
            elif el == "R":
                R_count += 1
                
            if L_count == R_count:
                bal_count += 1
                L_count = 0
                R_count = 0
                
        return bal_count