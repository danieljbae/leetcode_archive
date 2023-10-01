class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Brute force: time o(n^2)
        """
        n = len(nums)
        ret = []

        for i in range(n):
            val = 1
            for j in range(n):
                if i == j:
                    continue
                val = val * nums[j]
            ret.append(val)
        return ret



s = Solution()
print(s.productExceptSelf([1,2,3,4]))