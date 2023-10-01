class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str

        Analysis:
        - Time: O(n)
        - Space: O(n)
        """
        out = [""]*len(s)
        
        for i in range(len(s)):
            out[indices[i]] = s[i]
        
        return "".join(out)