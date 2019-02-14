class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        b0, b1 = 0, None
        dp = [[0, 0] for _ in range(len(prices))]
        b0 = 0
        b1 = None
        for i in range(1, len(prices)):
            dp[i][0] = max(prices[i] - prices[b0], dp[i-1][0])
            if b1:
                dp[i][1] = max(prices[i] - prices[b1] + dp[b1][0], dp[i-1][1])
            else:
                dp[i][1] = max(dp[i][0], dp[i-1][1])

            # update buy Idx
            if prices[i] < prices[b0]:
                b0 = i

            if b1 and - prices[i] + dp[i][0] > - prices[b1] + dp[b1][0]:
                    b1 = i
            else:
                if i > b0:
                    b1 = i

        return max(dp[-1][0], dp[-1][1])

class SolutionV1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        numStock = 1
        numTimes = 2
        dp = [[[0 for k in range(numStock + 1)] for j in range(numTimes + 1)] for i in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][0] = 0
        dp[0][0][1] = -prices[0]
        dp[0][1][1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(numTimes + 1):
                for k in range(numStock + 1):
                    hold = dp[i-1][j][k]
                    buy = dp[i-1][j][k-1] - prices[i] if k > 0 else -9999
                    sell = dp[i-1][j-1][k+1] + prices[i] if j > 0 and k < numStock else -9999
                    dp[i][j][k] = max(hold, buy, sell)
        res = 0
        for j in range(numTimes + 1):
            for k in range(numStock + 1):
                res = max(res, dp[-1][j][k])
        return res


class SolutionV2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        numStock = 1
        numTimes = 2
        dp = [[[0 for k in range(numStock + 1)] for j in range(numTimes + 1)] for i in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        dp[0][1][1], dp[0][2][1], dp[0][1][0], dp[0][2][0] = -9999, -9999, -9999, -9999
        for i in range(1, len(prices)):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])

            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])

            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][2][0] - prices[i])

        return max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0])


