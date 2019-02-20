class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        res = []
        self.dfs(res, 0, 0, n, '')
        return res
        

    def dfs(self, res, numL, numR, limit, curStr):
        if numL == numR == limit:
            res.append(curStr)
            return
        if numL < limit:
            self.dfs(res, numL+1, numR, limit, curStr + '(')
        if numR < numL and numR < limit:
            self.dfs(res, numL, numR+1, limit, curStr + ')')
        


class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        dp = [[]] * (n+1)
        dp[0].append('')
        for i in range(1, n+1):
            for k in range(0, i):
                for s1 in dp[k]:
                    for s2 in dp[i-k-1]:
                        dp[i].append('(' + s2 + ')' + s1)
        return dp[n]


        