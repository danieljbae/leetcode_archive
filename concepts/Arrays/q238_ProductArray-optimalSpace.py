class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Analysis
        Time: O(n) - iterate 2x for left products and right // merge products 
        Space: O(1) - output array does not count towards space complexity
        """
        n = len(nums)
        out = [1]*n
        
        # left loop
        out[0] = 1
        for i in range(1,n): # start at 1 (exclude head), bc product except self
            out[i] = nums[i-1] * out[i-1]
        
        # right loop // merge 
        r = 1
        for i in range(n-1,-1,-1): # start at n-2 (exclude tail), bc product except self
            out[i] = out[i] * r
            r *= nums[i]
        
        return out
        