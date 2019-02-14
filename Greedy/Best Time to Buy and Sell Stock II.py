class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :note: 1 time of buy or sell in a day
        """
        buy, sell = None, None
        lenP = len(prices)
        maxProfit = 0
        for idx, p in enumerate(prices):
            if buy is None:
                if idx + 1 == lenP or prices[idx + 1] <= p:
                    continue
                else:
                    buy = p
            else:
                if idx + 1 == lenP:
                    if p > buy:
                        maxProfit += p - buy
                    break
                elif prices[idx+1] >= p:
                    continue
                else:
                    maxProfit += p - buy
                    buy = None
        return maxProfit

class SolutionV1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :note: many times of buy or sell in a day
        """
        maxProfit = 0
        for idx, p in enumerate(prices):
            if idx > 0 and p > prices[idx - 1]:
                maxProfit += p - prices[idx - 1]
        return maxProfit



