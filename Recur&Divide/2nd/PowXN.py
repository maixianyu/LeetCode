class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if not x:
            return x
        if not n:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n != 1:
            if n & 1:
                res *= x
            x *= x
            n = n / 2

        res *= x
        return res


class SolutionV1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not x or n == 1:
            return x
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        res = self.myPow(x, n/2)
        return  res * res * (x if n & 1 else 1)

class SolutionV2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not x or n == 1:
            return x
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        return  x * self.myPow(x * x, n/2) if n & 1 else self.myPow(x * x, n/2)


class SolutionV3(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if not x:
            return x
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            if n & 1:
                res *= x
            x *= x
            n = n >> 1
        return res
