class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        :note: DFS
        """
        if not M:
            return 0
        height = len(M)
        count = 0
        for i in range(height):
            if M[i][i]:
                count += 1
                self._dfs(M, i, height)
        return count

    def _dfs(self, M, i, height):
        M[i][i] = None
        for idx in range(height):
            if M[i][idx] and M[idx][idx]:
                self._dfs(M, idx, height)


class SolutionV1(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        :note: union & find
        """
        if not M:
            return 0
        height = len(M)
        count = 0

        rel = [i for i in range(height)]

        for i in range(height):
            for fidx in range(i, height):
                if M[i][fidx]:
                    self._union(rel, i, fidx)

        res = set()
        for i in range(height):
            pi = rel[i]
            while pi != i:
                i = pi
                pi = rel[i]
            res.add(pi)
        return len(res)

    def _union(self, rel, i, j):
        pi = rel[i]
        while pi != i:
            i = pi
            pi = rel[i]

        pj = rel[j]
        while pj != j:
            j = pj
            pj = rel[j]

        rel[pj] = pi



