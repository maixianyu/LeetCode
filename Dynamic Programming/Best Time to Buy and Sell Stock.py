class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buyPrice = prices[0]
        res = 0
        profit = 0
        for p in prices[1:]:
            if p < buyPrice:
                buyPrice = p
            else:
                profit = p - buyPrice
                res = max(res, profit)
        return res

class SolutionV1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buyPrice = prices[0]
        dp = 0
        res = 0
        for p in prices[1:]:
            dp = max(p - buyPrice, dp)
            if p < buyPrice:
                buyPrice = p
        return dp
