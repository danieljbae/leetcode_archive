class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        
        Analysis: W.C is reverse strings, B.C. identical strings
        - Time: O(n + mk), where n is target and mk is source x iterations
        - Space: O(1)
        """
        t = 0
        count = 1
        t_len, s_len = len(target), len(source)
        
        while t < t_len:
            t_old = t
            for s in range(s_len):
                if source[s] == target[t]:
                    t += 1
                if t == len(target): # last char found
                    return count
            if t == t_old: # current target char, does not exist
                return -1
            count += 1
        
        return count 