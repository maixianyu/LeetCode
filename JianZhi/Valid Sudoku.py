class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.grid = [[set() for _ in range(3)] for _ in range(3)]
        self.getGridXY = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
        self.strNum = [str(i+1) for i in range(9)]
        for idxRow, row in enumerate(board):
            for idxCol, ele in enumerate(row):
                if ele != '.':
                    if ele not in self.row[idxRow] and ele not in self.col[idxCol] and ele not in self.grid[self.getGridXY[idxRow]][self.getGridXY[idxCol]]:
                        self.row[idxRow].add(ele)
                        self.col[idxCol].add(ele)
                        self.grid[self.getGridXY[idxRow]][self.getGridXY[idxCol]].add(ele)
                    else:
                        return False
        return True

