class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tot = 0 
        tot_array = []
        
        for i in range(0,len(nums)):
            tot += nums[i]
            tot_array.append(tot)
        return tot_array
            