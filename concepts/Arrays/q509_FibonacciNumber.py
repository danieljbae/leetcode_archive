class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        
        if N <= 1:
            return N
        else:
            return (self.fib(N-1) + self.fib(N-2))
         