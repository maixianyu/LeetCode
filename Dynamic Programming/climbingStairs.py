class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        f = [0, 1, 2]
        count = 3
        while count <= n:
            f.append(f[count-1] + f[count-2])
            count += 1
        return f[n]



class SolutionV1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        oneStepBefore = 2
        twoStepBefore = 1
        curSteps = 0
        for _ in range(2, n):
            curSteps = oneStepBefore + twoStepBefore
            oneStepBefore, twoStepBefore = curSteps, oneStepBefore
        return curSteps

