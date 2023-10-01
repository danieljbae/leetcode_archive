class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Runtime is O(n^2), O(n) outter loop and O(n) for inner loop or 2 Sum 

        Analysis
        Time: O(n^2) - 3sum iterates over all targets >> inner loop iterate over all pairs via 2Sum
        Space: O(n) - storing all nums in hashset via 2sum functions 
        """
        
        
        nums.sort() # Sort list, as 2Sum method requires 2 pointers to go inwards 
        ans_set = set()
        
        # Loop through all elements and fix the inverse of the head (Inverse as we want a 3sum of Zero) 
        for idx, val in enumerate(nums):
            self.twoSum(nums[idx+1:],-val,ans_set) # no return value needed
        return ans_set
    
    
    
    
    def twoSum(self, nums, target,ans_set):
        """
        By fixing the head of the list, we can use the logic of 2Sum to find all pairs of 
        numbers whose sum is the inverse. Giving us a total sum of zero among the 3 numbers 
        
        nums: list of numbers, excluding the value that is being fixed
        target: the inverse fixed value, as any two numbers that's sum equals the inverse of the target, will equate to zero
        ans_set: a set to contain all unique triplets  
        """
        
        diff_hashmap = {}
        
        for idx,val in enumerate(nums):
            # if the remaining triplet is in our sublist (excluding target value or head)
            if target-val in diff_hashmap:
                ans_set.add((-target,val,target-val)) # Notice: we are adding all  for 3Sum solution, as only triplets that sum to 0 are valid 
            # intialize hash map with every possible remaining triplet value in sublist
            diff_hashmap[val] = idx 
        return ans_set
                