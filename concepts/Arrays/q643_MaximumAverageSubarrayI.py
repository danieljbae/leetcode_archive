class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        curr_max = sum(nums[0:k])
        total_max = curr_max
        
        for i in range(len(nums)-k):
            curr_max -= nums[i] # remove head of old window
            curr_max += nums[i+k] # add tail of new window
            total_max = max(curr_max, total_max) 
        
        return 1.0 * total_max/k
        
        