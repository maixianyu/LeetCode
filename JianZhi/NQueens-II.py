class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = 0
        self._solve(n, [], [])
        return self.res

    def _solve(self, n, pos):
        if len(pos) == n:
            self.res += 1
        for p in range(n):
            curIdx = len(pos)
            if p not in pos:
                if not pos:
                    self._solve(n, [p])
                elif pos:
                    b = True
                    for idx, preP in enumerate(pos):
                        b = b & (abs(p - preP) != (curIdx - idx))
                        if not b:
                            break
                        else:
                            if idx == curIdx - 1:
                                self._solve(n, pos + [p])
