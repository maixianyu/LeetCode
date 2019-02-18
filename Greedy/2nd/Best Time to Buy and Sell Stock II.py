class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        prev = prices[0]
        for p in prices[1:]:
            if p > prev:
                res += p - prev
            prev = p
        return res