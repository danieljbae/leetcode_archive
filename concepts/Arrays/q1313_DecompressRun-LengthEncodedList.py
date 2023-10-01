class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(0,len(nums),2):
            ret += [nums[i+1]]*nums[i]
        return ret