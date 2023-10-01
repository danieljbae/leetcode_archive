class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Analysis
        Time: O(n log n) - sorting list, requisite for 2-pointer approach
        Space: O(n) - storing all nums in hashset
        """
        nums = enumerate(nums) # to preserve orginal indexes before sorting (idx, val)
        nums = sorted(nums, key = lambda x:x[1]) # sort for 2-pointer approach (sort by val)
        
        p1,p2 = 0, len(nums) - 1
        
        while p1 < p2:
            if nums[p1][1] + nums[p2][1] == target:
                return [nums[p1][0], nums[p2][0]]
            
            # sort to determine which pointer to incrument 
            elif nums[p1][1] + nums[p2][1] < target: 
                p1 += 1 
            else:
                p2 -= 1
             