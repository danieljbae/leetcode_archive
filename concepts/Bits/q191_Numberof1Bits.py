class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        Analysis: Hamming weight
        - Time: O(n)
        - Space: O(1)
        source: https://expobrain.net/2013/07/29/hamming-weights-python-implementation/#:~:text=Counting%20the%20number%20of%201's,implementations%20are%20obviously%20excluded%20%3A%2D)%20)
        """       
        c = 0
        while n:
            n &= n - 1
            c += 1

        return c

        # python specific approach - one liner 
        # return bin(x).count("1")