class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.grid = [[set() for _ in range(3)] for _ in range(3)]
        self.unfilled = []
        self.getGridXY = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
        self.strNum = [str(i+1) for i in range(9)]
        for idxRow, row in enumerate(board):
            for idxCol, ele in enumerate(row):
                if ele != '.':
                    self.row[idxRow].add(ele)
                    self.col[idxCol].add(ele)
                    self.grid[self.getGridXY[idxRow]][self.getGridXY[idxCol]].add(ele)
                else:
                    self.unfilled.append((idxRow, idxCol))
        b = self._solve(self.unfilled, board)
        print(b)
        print(board)

    def _solve(self, unfilled, board):
        if not unfilled:
            return True
        x, y = unfilled[0]
        for num in self.strNum:
            if num not in self.col[y] and num not in self.row[x] and num not in self.grid[self.getGridXY[x]][self.getGridXY[y]]:
                self.col[y].add(num)
                self.row[x].add(num)
                self.grid[self.getGridXY[x]][self.getGridXY[y]].add(num)

                if self._solve(unfilled[1:], board):
                    board[x][y] = num
                    return True

                self.col[y].remove(num)
                self.row[x].remove(num)
                self.grid[self.getGridXY[x]][self.getGridXY[y]].remove(num)

        return False

class SolutionV1(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.strNum = [str(i+1) for i in range(9)]
        self.col = [set() for _ in range(9)]
        self.rowRm = [set(self.strNum) for _ in range(9)]
        self.grid = [[set() for _ in range(3)] for _ in range(3)]
        self.unfilled = []
        self.getGridXY = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
        for idxRow, row in enumerate(board):
            for idxCol, ele in enumerate(row):
                if ele != '.':
                    self.rowRm[idxRow].remove(ele)
                    self.col[idxCol].add(ele)
                    self.grid[self.getGridXY[idxRow]][self.getGridXY[idxCol]].add(ele)
                else:
                    self.unfilled.append((idxRow, idxCol))
        b = self._solve(self.unfilled, board)
        print(b)
        print(board)

    def _solve(self, unfilled, board):
        if not unfilled:
            return True
        x, y = unfilled[0]
        for num in self.rowRm[x]:
            if num not in self.col[y] and num not in self.grid[self.getGridXY[x]][self.getGridXY[y]]:
                self.col[y].add(num)
                self.rowRm[x].remove(num)
                self.grid[self.getGridXY[x]][self.getGridXY[y]].add(num)

                if self._solve(unfilled[1:], board):
                    board[x][y] = num
                    return True

                self.col[y].remove(num)
                self.rowRm[x].add(num)
                self.grid[self.getGridXY[x]][self.getGridXY[y]].remove(num)

        return False

