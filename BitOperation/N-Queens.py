class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.N = n
        self._dfs(0, 0, 0, 0, [])
        return [[self.genStr(i) for i in plist] for plist in self.res]

    def genStr(self, i):
        count = 0
        res = ''
        while count < self.N:
            if i & 1:
                res = res + 'Q'
            else:
                res = res + '.'
            i = i >> 1
            count += 1
        return res


    def _dfs(self, row, col, pie, na, posList):
        if row == self.N:
            self.res.append(posList)

        bits = (~(col | pie | na)) & ((1 << self.N) - 1)
        while bits:
            p = bits & -bits
            self._dfs(row + 1, col | p, (pie | p) << 1, (na | p) >> 1, posList + [p])
            bits = bits & (bits - 1)