class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    
        Warm up for "424. Longest Repeating Character Replacement"

        Analysis: 
        - Time: O(n) 
        - Space: O(n) w/ extra base case || O(1) without
        """
        n = len(nums)
        
        # Base case
        if not nums:
            return 0
        
        # Extra base case to optimize if list is all same value    
        if len(set(nums)) == 1:
            if 1 in set(nums):
                return n
            else:
                return 0
        
        globalMax = localMax = 0
        for num in nums:
            if num == 1:
                localMax += 1
                globalMax = max(localMax,globalMax)
            else:
                localMax = 0

        return globalMax