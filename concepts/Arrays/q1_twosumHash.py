class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Analysis
        Time: O(n^2) - Iterate over all numbers 1x to see if diff exists (target-num[i]) 
        Space: O(n) - storing all nums in hashmap
        """
        diff_d  = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in diff_d:
                return [diff_d[target - nums[i]],i ]
            else:
                diff_d[nums[i]] = i
                