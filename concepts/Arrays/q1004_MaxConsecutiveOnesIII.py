class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        
        Analysis: Sliding window
        - Time = O(n)
        - Space = O(1) 
        """
        # K is our buffer or number of operations alotted
        maxOnes = 0
        numZeros = 0
        start = 0
        
        for end in range(len(A)):
            if A[end] == 0:
                numZeros += 1
            
            # shrink window per buffer
            while numZeros > K:
                if A[start] == 0:
                    numZeros -= 1 
                start += 1
                
            maxOnes = max(end-start+1, maxOnes)
            
        return  maxOnes