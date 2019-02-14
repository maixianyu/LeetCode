class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        GotOne = False
        while n and not GotOne:
            GotOne = n & 1
            n = n >> 1
        return n == 0



class SolutionV1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        n = n & (n - 1)
        return n == 0
