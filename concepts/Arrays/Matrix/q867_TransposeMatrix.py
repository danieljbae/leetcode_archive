class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n_row,n_col = len(A),len(A[0])
        ret_matrix = [[None]*n_row for i in range(n_col)] # swapped outter and inner loop variables, to flip x and y axis of output matrix  
        
        
        for r,row in enumerate(A): # loop through each row
            for c,val in enumerate(A[r]): # on each row, loop through all columns
                ret_matrix[c][r] = val # swapped col and row index, such that values have been transposed
        
        return ret_matrix
                
                
            
                
                
        