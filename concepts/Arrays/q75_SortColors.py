class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Analysis: 2-pointer variant, 3-way quicksort partitioning
        - Time: O(n)
        - Space: O(1)
        """
        n = len(nums)
        
        # Keep track of beg group's tail & last group's head
        begTail = curr = 0 
        endHead = n - 1
        
        while curr <= endHead:
            # move to tail of beg group
            if nums[curr] == 0:
                nums[curr], nums[begTail] = nums[begTail], nums[curr]
                begTail += 1
                curr += 1
            # move to head of end group
            elif nums[curr] == 2:
                nums[curr], nums[endHead] = nums[endHead], nums[curr]
                endHead -= 1
            else:
                curr += 1
        

        '''
        Input:  nums = [2,0,2,1,1,0]
        Output: nums = [0,0,1,1,2,2]
        
        _____________________________________________
        Initial
        curr = 0
        red_end = 0
        blue_end = 5
         
         c
         r         b
        [2,0,2,1,1,0]
        
        
        _____________________________________________
        Iteration Count (1)
        
        curr = 0
        red_end = 0
        blue_end = 4
        
        c
        r        b
        [0,0,2,1,1,2]
        
        elif: swap with beg of back, increase back window
        
        _____________________________________________
        Iteration Count (2)
        
        curr = 0
        red_end = 0
        blue_end = 4
        
         c
         r       b
        [0,0,2,1,1,2]
        
        else: traverse
        
        _____________________________________________
        Iteration Count (3)
        
        curr = 1
        red_end = 0
        blue_end = 4
        
           c
         r       b
        [0,0,2,1,1,2]
        
        
        if: swap with end of front
        
        _____________________________________________
        Iteration Count (4)
        
        curr = 2
        red_end = 1
        blue_end = 4
        
             c
           r     b
        [0,0,2,1,1,2]
        
        
        elif: swap with beg of back, increase back window

        _____________________________________________
        Iteration Count (5)
        
        curr = 2
        red_end = 1
        blue_end = 3
        
             c
           r   b
        [0,0,1,1,2,2]
        
        
        elif: swap with beg of back, increase back window
        
        '''
    