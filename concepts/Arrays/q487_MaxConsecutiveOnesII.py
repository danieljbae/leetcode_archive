class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Analysis: Sliding Window approach
        - Time: O(n)
        - Space: O(1) 
        """
        maxOnes = 0 
        zeroCount = 0
        k = 1 # buffer, 1 flip limit
        start = 0
        
        
        for end in range(len(nums)):
            if nums[end] == 0:
                zeroCount += 1
            
            # Exceeds buffer limit, so shrink start of window - which removes extra number of zeros
            while zeroCount > k: 
                if nums[start] == 0:
                    zeroCount -= 1
                
                start += 1
                
            maxOnes = max(maxOnes, end-start+1)
        
        return maxOnes