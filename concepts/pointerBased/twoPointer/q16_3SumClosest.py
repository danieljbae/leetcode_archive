class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        nums = [-1,2,1,-4], target = 1
        output = 2

        explanation: the sum that is closest to the target is 2 = -1 + 2 + 1 
        __________________________________________________________________

        target = 1

         i    l     r
        [-4, -1, 1, 2]

        for loop to hold i constant
            curr_sum = sum(nums[i], nums[l], nums[r]) = -3


            while loop and perform 2 pointer to search for closest difference

                curr_diff = abs(target-curr_sum)

                if curr_diff < closest_diff:
                    closest_sum = curr_sum

                search for next closest diff with i being held as constant

        """
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i, num in enumerate(nums[:-2]):
            left, right = i+1, n-1
            # Hold i constant and Use 2-pointer to find closest difference
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                # Update output, if closer difference found
                if abs(target-curr_sum) < abs(target-closest_sum):
                    closest_sum = curr_sum
                # Search for next closer difference
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                # Found triplet that equals target
                else:
                    return closest_sum

        return closest_sum
