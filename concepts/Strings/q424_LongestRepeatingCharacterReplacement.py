class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        
        Analysis: Sliding window w/ Auxiliary stucture 
        - Time = O(n)
        - Space = O(n) 
        """
        start = 0
        c_freq = {}
        longest_str = 0 
        
        for end in range(len(s)):
            
            # intialize char map
            if s[end] not in c_freq:
                c_freq[s[end]] = 0
            c_freq[s[end]] += 1
            
            window_len = end - start + 1
            replacement_cost = window_len - max(c_freq.values())
            
            # within buffer limit: update global var
            if replacement_cost <= k:
                # print(f'window size: {window_len}, \t replacement cost: {replacement_cost}')
                longest_str = window_len # max(window_len, replacement_cost)
            
            # exceed buffer: shrink window via freq map
            else: 
                c_freq[s[start]] -= 1
                if not c_freq[s[start]]:
                    c_freq.pop(s[start])
                start += 1
                
        return longest_str