class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sorted_nums = sorted(nums) # O(n log n)
        
        # create hash map, for constant access time to sorted index positions - O(n)
        hash_numCount = {}
        for idx,val in enumerate(sorted_nums):
            if val in hash_numCount:
                continue
            else: # intialize with nums index as dictionary value
                hash_numCount[val] = idx 
        
        # output list and reference hash map for constant acess time - O(n)
        out = [0]*n
        for i in range(n):
            out[i] = hash_numCount[nums[i]]
            
        return out