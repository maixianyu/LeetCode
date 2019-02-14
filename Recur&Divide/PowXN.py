class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0.0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        # odd
        if n % 2:
            return x * self.myPow(x, n - 1)
        else:
            res = self.myPow(x, n / 2)
            return res * res

class SolutionV1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0.0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = self.myPow(x, n / 2)
        return x * res * res if n % 2 else res * res


class SolutionV2(object):
    """iter Version"""
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0.0:
            return 0.0
        if n < 0:
            n = -n
            x = 1 / x
        res = 1
        while n:
            # odd
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
