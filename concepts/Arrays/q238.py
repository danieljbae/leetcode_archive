class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        # answer Array contains products to left of i'th element O(n) 
        answer = [0]*len(nums)
        answer[0] = 1  # intitialize with 1 bc no product exists before head of list
        for i in range(1,len(nums)): # Skip head, so start at 1
            answer[i] = nums[i-1] * answer[i-1] # index i-1 we are concerned with
                                                # products to left of cursor value 
        
        
        # Update our answer array with right products  
        R = 1 # use variable to keep track of culative product total 
        for i in range(len(nums)-1,-1,-1): # Do not skip tail, so start at n-1
            answer[i] = (answer[i]*R)
            R *= nums[i] 
            
        return answer
                
        