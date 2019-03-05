class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        self.N = n
        self.res = []
        shu, pie, na = set(), set(), set()
        self._dfs(0, shu, pie, na, [])
        return [["." * x + "Q" + "." * (n - x - 1) for x in l] for l in self.res]

    def _dfs(self, x, shu, pie, na, tmpRes):
        if x == self.N:
            self.res.append(tmpRes)
        for y in range(self.N):
            pieTmp, naTmp = x + y, y - x
            if y not in shu and pieTmp not in pie and naTmp not in na:
                shu.add(y)
                pie.add(pieTmp)
                na.add(naTmp)
                self._dfs(x+1, shu, pie, na, tmpRes + [y])
                shu.remove(y)
                pie.remove(pieTmp)
                na.remove(naTmp)



class SolutionV1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        self.N = n
        shu = [False] * n
        pie = [False] * (2 * n - 1)
        na = [False] * (2 * n - 1)
        self.res = []
        self._dfs(0, shu, pie, na, [])
        return [["." * x + "Q" + "." * (n - x - 1) for x in l] for l in self.res]

    def _dfs(self, x, shu, pie, na, resTmp):
        if x == self.N:
            self.res.append(resTmp)
            return
        for y in range(self.N):
            pieIdx, naIdx = x + y, y - x + self.N - 1 
            if shu[y] or pie[pieIdx] or na[naIdx]:
                continue
            shu[y] = pie[pieIdx] = na[naIdx] = True
            self._dfs(x+1, shu, pie, na, resTmp + [y])
            shu[y] = pie[pieIdx] = na[naIdx] = False
                
class SolutionV2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        self.N = n
        shu = 0
        pie = 0
        na = 0
        self.res = []
        self._dfs(0, shu, pie, na, [])
        return [["." * x + "Q" + "." * (n - x - 1) for x in l] for l in self.res]

    def _dfs(self, x, shu, pie, na, resTmp):
        if x == self.N:
            self.res.append(resTmp)
            return
        for y in range(self.N):
            pieIdx, naIdx = x + y, y - x + self.N - 1 
            if ((shu >> y) | (pie >> pieIdx) | (na >> naIdx)) & 1:
            #if (shu >> y) | (pie >> pieIdx) | (na >> naIdx):   not working .. !
                continue
            shu ^= (1 << y); pie ^= (1 << pieIdx); na ^= (1 << naIdx)
            self._dfs(x+1, shu, pie, na, resTmp + [y])
            shu ^= (1 << y); pie ^= (1 << pieIdx); na ^= (1 << naIdx)
            
from math import log
class SolutionV3(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        self.N = n
        shu = 0
        pie = 0
        na = 0
        self.res = []
        self._dfs(0, shu, pie, na, [])
        return [["." * x + "Q" + "." * (n - x - 1) for x in l] for l in self.res]

    def _dfs(self, x, shu, pie, na, resTmp):
        if x == self.N:
            self.res.append(resTmp)
            return
        available = ((1<<self.N) - 1) & ~(shu | (pie >> (x)) | (na >> (self.N - 1 - x)))
        while available:
            pos = available & (-available)
            available ^= pos
            shu ^= pos; pie ^= (pos << x); na ^= (pos << (self.N - 1 - x))
            self._dfs(x+1, shu, pie, na, resTmp + [int(log(pos, 2))])
            shu ^= pos; pie ^= (pos << x); na ^= (pos << (self.N - 1 - x))

class SolutionV4(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        self.N = n
        shu = 0
        pie = 0
        na = 0
        self.res = []
        self._dfs(0, shu, pie, na, [])
        return [["." * x + "Q" + "." * (n - x - 1) for x in l] for l in self.res]

    def _dfs(self, x, shu, pie, na, resTmp):
        if x == self.N:
            self.res.append(resTmp)
            return
        available = ((1<<self.N) - 1) & ~(shu | pie | na)
        while available:
            pos = available & (-available)
            available ^= pos
            self._dfs(x+1, shu | pos, (pie | pos) << 1, (na | pos) >> 1, resTmp + [int(log(pos, 2))])



