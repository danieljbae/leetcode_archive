class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)


        # transpose matrix
        for i in range(n):
            for j in range(i,len(matrix[i])): # set to i, to not swap Main Diagnol
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # adjust column ordering
        for i in range(n):
            for j in range(len(matrix[i])//2): # set to j//2 bc swapping midpoint 
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1] , matrix[i][j]