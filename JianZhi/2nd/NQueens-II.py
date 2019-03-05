from math import log
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return 0
        self.N = n
        shu, pie, na = 0, 0, 0
        self.res = 0
        self._dfs(0, shu, pie, na)
        return self.res

    def _dfs(self, x, shu, pie, na):
        if x == self.N:
            self.res += 1
            return
        available = ((1<<self.N) - 1) & ~(shu | pie | na)
        while available:
            pos = available & (-available)
            available ^= pos
            self._dfs(x+1, shu | pos, (pie | pos) << 1, (na | pos) >> 1)
