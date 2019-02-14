class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount == 0:
            return 0
        dp = [999 for _ in range(amount+1)]
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != 999 else -1

class SolutionV1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount == 0:
            return 0
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1
