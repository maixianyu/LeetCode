class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [0] * 9
        col = [0] * 9
        #grid = [[0] * 3] * 3
        grid = [[0, 0, 0] for _ in range(3)]

        for rIdx, r in enumerate(board):
            for cIdx, c in enumerate(r):
                if c != '.':
                    val = ord(c) - ord('1')
                    if ((row[rIdx] >> val)\
                         | (col[cIdx] >> val) | (grid[rIdx/3][cIdx/3] >> val)) & 1:
                        return False
                    else:
                        ele = 1<<val
                        row[rIdx] |= ele
                        col[cIdx] |= ele
                        grid[rIdx/3][cIdx/3] |= ele
        return True