class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        self.bWidth = len(board[0])
        self.bHeight = len(board)
        bMap = dict()
        for rIdx, row in enumerate(board):
            for cIdx, ele in enumerate(row):
                if ele in bMap:
                    bMap[ele].append((rIdx, cIdx))
                else:
                    bMap[ele] = [(rIdx, cIdx)]

        self.visited = set()
        self.res = set()
        for w in words:
            c = w[0]
            if c in bMap:
                for rIdx, cIdx in bMap[c]:
                    self.visited = set()
                    self.visited.add("%d,%d" % (rIdx, cIdx))
                    if self.recur(rIdx, cIdx, w, w[1:], board):
                        self.res.add(w)

        return list(self.res)

    def recur(self, rIdx, cIdx, word, wordRemaing, board):
        if not wordRemaing:
            return True

        # test up
        for rIdxTemp, cIdxTemp in [(rIdx-1, cIdx), (rIdx+1, cIdx), (rIdx, cIdx-1), (rIdx, cIdx+1)]:
            if (rIdxTemp >= 0) and rIdxTemp < self.bHeight and cIdxTemp >= 0 and cIdxTemp < self.bWidth:
                if (board[rIdxTemp][cIdxTemp] == wordRemaing[0]):
                    if "%d,%d" % (rIdxTemp, cIdxTemp) not in self.visited:
                        self.visited.add("%d,%d" % (rIdxTemp, cIdxTemp))
                        if self.recur(rIdxTemp, cIdxTemp, word, wordRemaing[1:], board):
                            return True
                        self.visited.remove("%d,%d" % (rIdxTemp, cIdxTemp))



class SolutionV1(object):
    def findWords(self, board, words):
        """
        :note: DFS + Trie
        """
        if not board or not words:
            return []

        # construct Trie Tree
        self.root = dict()
        self.res = set()
        root = self.root
        for w in words:
            root = self.root
            for c in w:
                root = root.setdefault(c, dict())
            root.setdefault('#', True)

        # loop board
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.height = len(board)
        self.width = len(board[0])
        for rIdx in range(self.height):
            for cIdx in range(self.width):
                if board[rIdx][cIdx] in self.root:
                    board[rIdx][cIdx], tmp = '@', board[rIdx][cIdx]
                    self._dfs(rIdx, cIdx, tmp, self.root[tmp], board)
                    board[rIdx][cIdx] = tmp
        return list(self.res)

    def _dfs(self, x, y, resStr, root, board):
        if '#' in root:
            self.res.add(resStr)
        for i in range(4):
            dx, dy = self.dx[i], self.dy[i]
            if x + dx >= 0 and x + dx < self.height and y + dy >= 0 and y + dy < self.width\
                and board[x+dx][y+dy] in root:
                board[x+dx][y+dy], tmp = '@', board[x+dx][y+dy]
                self._dfs(x+dx, y+dy, resStr + tmp, root[tmp], board)
                board[x+dx][y+dy] = tmp


class SolutionV2(object):
    def findWords(self, board, words):
        """
        :note: DFS + Trie
        """
        if not board or not words:
            return []

        # construct Trie Tree
        self.root = dict()
        self.res = set()
        root = self.root
        for w in words:
            root = self.root
            for c in w:
                root = root.setdefault(c, dict())
            root.setdefault('#', True)

        # loop board
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.height = len(board)
        self.width = len(board[0])
        for rIdx in range(self.height):
            for cIdx in range(self.width):
                if board[rIdx][cIdx] in self.root:
                    self._dfs(rIdx, cIdx, board[rIdx][cIdx], self.root[board[rIdx][cIdx]], board)
        return list(self.res)

    def _dfs(self, x, y, resStr, root, board):
        if '#' in root:
            self.res.add(resStr)
        board[x][y], tmp = '@', board[x][y]
        for i in range(4):
            dx, dy = self.dx[i], self.dy[i]
            if x + dx >= 0 and x + dx < self.height and y + dy >= 0 and y + dy < self.width \
                    and board[x+dx][y+dy] in root:
                self._dfs(x+dx, y+dy, resStr + board[x+dx][y+dy], root[board[x+dx][y+dy]], board)
        board[x][y] = tmp

