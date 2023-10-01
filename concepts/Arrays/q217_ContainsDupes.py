class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Analysis
        Time: O(n) - iterate over all nums to gather size 
        Space: O(n) - set for nums to compare sizes 
        """
        return len(nums) != len(set(nums)) 



        #Brute Force 1: Compare all pairs 
        # Time O(n^2), Space O(1)

        # Sub optimal 2: Sort then loop and check (i+1) element
        # Time O(n log n), Space O(1)