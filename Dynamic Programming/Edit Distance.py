class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        maxlen = len(word1) + len(word2)

        dp = [[max(i, j) if i == 0 or j == 0 else maxlen for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + 1, dp[i][j+1] + 1, dp[i+1][j] + 1)
        return dp[-1][-1]



class SolutionV1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        m, n = len(word1), len(word2)
        maxlen = m + n

        dp = [[maxlen for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i
        for i in range(n + 1): dp[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]
