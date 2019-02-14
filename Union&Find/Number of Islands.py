class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        :note: DFS
        """
        if not grid or not grid[0]:
            return 0
        height, width = len(grid), len(grid[0])
        root = grid[:]
        count = 0
        for i in range(height):
            for j in range(width):
                if root[i][j] == '1':
                    count += 1
                    self._dfs(root, i, j, height, width)
        return count

    def _dfs(self, root, i, j, h, w):
        root[i][j] = '0'
        if i + 1 < h and root[i+1][j] == '1':
            self._dfs(root, i + 1, j, h, w)
        if i - 1 >= 0 and root[i-1][j] == '1':
            self._dfs(root, i - 1, j, h, w)
        if j + 1 < w and root[i][j+1] == '1':
            self._dfs(root, i, j + 1, h, w)
        if j - 1 >= 0 and root[i][j-1] == '1':
            self._dfs(root, i, j - 1, h, w)


class SolutionV1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        :note: BFS
        """
        if not grid or not grid[0]:
            return 0
        height, width = len(grid), len(grid[0])
        root = grid[:]
        count = 0
        q = []
        for i in range(height):
            for j in range(width):
                if root[i][j] == '1':
                    q.append((i, j))
                    root[i][j] = '0'
                    count += 1
                while q:
                    ii, jj = q.pop(0)
                    if ii - 1 >= 0 and root[ii-1][jj] == '1':
                        q.append((ii - 1, jj))
                        root[ii-1][jj] = '0'
                    if ii + 1 < height and root[ii+1][jj] == '1':
                        q.append((ii + 1, jj))
                        root[ii+1][jj] = '0'
                    if jj - 1 >= 0 and root[ii][jj-1] == '1':
                        q.append((ii, jj - 1))
                        root[ii][jj-1] = '0'
                    if jj + 1 < width and root[ii][jj+1] == '1':
                        q.append((ii, jj + 1))
                        root[ii][jj+1] = '0'

        return count


class SolutionV2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        :note: Union & Find
        """
        if not grid or not grid[0]:
            return 0
        height, width = len(grid), len(grid[0])
        root = [[(i, j) if grid[i][j] == '1' else None for j in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                if root[i][j]:
                    if i + 1 < height and root[i+1][j]:
                        self._union(root, i, j, i + 1, j)
                    if j + 1 < width and root[i][j+1]:
                        self._union(root, i, j, i, j + 1)

        res = set()
        for i in range(height):
            for j in range(width):
                if root[i][j]:
                    pi, pj = self._findroot(root, i, j)
                    res.add("%d,%d" % (pi, pj))

        return len(res)

    def _union(self, root, i, j, x, y):
        ri, rj = self._findroot(root, i, j)
        rx, ry = self._findroot(root, x, y)
        root[rx][ry] = (ri, rj)

    def _findroot(self, root, i, j):
        if root[i][j] == (i, j):
            return (i, j)
        else:
            pi, pj = root[i][j]
            return self._findroot(root, pi, pj)



