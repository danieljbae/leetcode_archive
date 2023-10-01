class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Analysis
        Time: O(n) - iterate 3x for left product, right product, and merge products 
        Space: O(2n) - left and right product arrays(parition left pivot)
        """
        n = len(nums)
        
        # left product array
        ls_left = [1]*n
        for i in range(1,n): # start at 1 (exclude head), bc product except self
            ls_left[i] = ls_left[i-1]*nums[i-1]
            
            
        # right product array
        ls_right = [1]*n
        for i in range(n-2,-1,-1): # start at n-2 (exclude tail), bc product except self
            ls_right[i] = ls_right[i+1]*nums[i+1] 
        
        # final merged array
        out = [1]*n
        for i in range(n):
            out[i] = ls_left[i] * ls_right[i]
        
        return out

t = Solution()
print(t.productExceptSelf([1,2,3,4]))