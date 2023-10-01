class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Analysis
        Time: O(n) - iterate over all prices
        Space: O(1) - just storing variables, nothing scaling by prices list
        """
        maxProfit = 0
        minBuy = float('inf')
        
        for price in prices: 
            minBuy = min(minBuy,price) 
            maxProfit = max(price-minBuy,maxProfit)
        return maxProfit
        