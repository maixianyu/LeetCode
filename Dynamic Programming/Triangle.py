class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        dist = triangle[-1]
        num = n - 1
        while num > 0:
            idx = 0
            while idx < num:
                dist[idx] = min(dist[idx], dist[idx+1]) + triangle[num - 1][idx]
                idx += 1
            num -= 1
        return dist[0]

class SolutionV1(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dist = triangle[-1]
        for rowIdx in range(len(triangle) - 2, -1, -1):
            for colIdx in range(len(triangle[rowIdx])):
                dist[colIdx] = min(dist[colIdx], dist[colIdx+1]) + triangle[rowIdx][colIdx]
        return dist[0]


