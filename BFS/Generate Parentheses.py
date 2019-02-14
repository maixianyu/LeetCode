class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.maxLevel = n * 2
        self.N = n
        self.array = [None for i in range(self.maxLevel)]
        self.res = []
        self.recur(-1, None, 0, 0)
        transList = map(lambda l: ''.join(map(lambda ele: '(' if ele else ')', l)), self.res)
        return transList

    def recur(self, preLevel, choice, numT, numF):
        curLevel = preLevel + 1
        if curLevel > self.maxLevel:
            return
        if curLevel >= 1:
            self.array[curLevel-1] = choice

        if curLevel == self.maxLevel and self.isGood(self.array, self.maxLevel):
            self.res.append(self.array[:])
            return
        elif numT > self.N:
            return
        elif numF > self.N:
            return

        self.recur(curLevel, True, numT + 1, numF)
        self.recur(curLevel, False, numT, numF + 1)


    def isGood(self, array, num):
        """
        :param array: list[Bool]
        :return: Bool
        """
        stack = []
        for idx in range(num):
            b = array[idx]
            if stack:
                if stack[-1] and not b:
                    stack.pop(-1)
                else:
                    stack.append(b)
            else:
                stack.append(b)

        if stack:
            return False
        else:
            return True

class SolutionV1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.maxLevel = n * 2
        self.array = [None for i in range(self.maxLevel+1)]
        self.res = []
        self.recur(-1, None, 0, 0)
        return self.res

    def recur(self, preLevel, choice, numT, numF):
        if numF > numT:
            return
        curLevel = preLevel + 1
        self.array[curLevel-1] = choice
        if curLevel == self.maxLevel:
            if numF == numT:
                self.res.append(''.join(self.array[:self.maxLevel]))
            return

        self.recur(curLevel, '(', numT + 1, numF)
        self.recur(curLevel, ')', numT, numF + 1)


class SolutionV2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.N = n
        self.maxLevel = n * 2
        self.res = []
        self.recur(0, 0, '')
        return self.res

    def recur(self,numT, numF, strRes):
        if numF == self.N and numT == self.N:
            self.res.append(strRes)
            return

        if numT < self.N:
            self.recur(numT + 1, numF, strRes + '(')
        if numF < numT and numF < self.N:
            self.recur(numT, numF + 1, strRes + ')')

