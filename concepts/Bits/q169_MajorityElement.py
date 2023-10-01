class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Analysis: Non-optimal w/ Hashmap
        - Time: O(n) 
        - Space: O(n) 
        """
        n = len(nums) 
        if n == 1:
            return nums[0]
        
        
        thresh = n//2
        d = {}
        for i in range(n):
            if nums[i] in d:
                d[nums[i]] += 1
                if d[nums[i]] > thresh:
                    return nums[i]
            else: 
                d[nums[i]] = 1
        
                
        