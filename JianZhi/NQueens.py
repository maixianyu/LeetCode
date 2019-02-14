class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.qMap = dict()
        for i in range(n):
            self.qMap[i] = self._genQ(n, i)
        self._solve(n, [], [])
        return self.res

    def _solve(self, n, pos, strList):
        if len(pos) == n:
            self.res.append(strList)
        for p in range(n):
            curIdx = len(pos)
            if p not in pos:
                if not pos:
                    self._solve(n, [p], strList + [self.qMap[p]])
                elif pos:
                    b = True
                    for idx, preP in enumerate(pos):
                        b = b & (abs(p - preP) != (curIdx - idx))
                        if not b:
                            break
                        else:
                            if idx == curIdx - 1:
                                self._solve(n, pos + [p], strList + [self.qMap[p]])

    def _genQ(self, n, p):
        res = ''
        for i in range(n):
            if i != p:
                res += '.'
            else:
                res += 'Q'
        return res


class SolutionV1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.col = set()
        self.pie = set()
        self.la = set()
        self._solve(n, 0, [])
        return [['.' * p + 'Q' + '.' * (n - p - 1) for p in posList] for posList in self.res]

    def _solve(self, n, row, pos):
        if row == n:
            self.res.append(pos)
            return

        for col in range(n):
            if col not in self.col and col + row not in self.pie and col - row not in self.la:
                self.col.add(col)
                self.pie.add(col + row)
                self.la.add(col - row)

                self._solve(n, row + 1, pos + [col])

                self.col.remove(col)
                self.pie.remove(col + row)
                self.la.remove(col - row)


class SolutionV2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self._solve(n, [], [], [])
        return [['.' * p + 'Q' + '.' * (n - p - 1) for p in posList] for posList in self.res]

    def _solve(self, n, col, pie, la):
        curRow = len(col)
        if curRow == n:
            self.res.append(col)
            return
        for p in range(n):
            if p not in col and p + curRow not in pie and p - curRow not in la:
                self._solve(n, col + [p], pie + [p + curRow], la + [p - curRow])

