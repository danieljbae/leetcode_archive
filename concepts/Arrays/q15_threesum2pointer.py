class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Analysis
        Time: O(n^2) - outter loop, 3sum, iterates over all targets >> inner loop iterate over all pairs via 2Sum
        Space: O(1) - 2 pointer does not allocate more memory
        """
        nums.sort()
        n, ans = len(nums), set()
        
        for i in range(n): # outter loop holds Target constant
            if i > 0 and nums[i] == nums[i-1]: continue # No value in sorted ls is big enough, such that "C" -> -(A+B) == C or (-A*2) == C
            
            target = -nums[i]            
            l, r = i+1, n-1
            
            while l < r: # 2-pointer loop
                if nums[l] + nums[r] == target:
                    ans.add((-target,nums[l],nums[r]))
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans
        