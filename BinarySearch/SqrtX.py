class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) / 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif right - left == 1:
                if right * right == x:
                    return right
                else:
                    return left
            elif tmp < x:
                left = mid
            else:
                right = mid


class SolutionV1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        :note: slower, but clearer
        """
        if x == 0 or x == 1: return x
        left, right = 1, x - 1
        res = 0
        while left <= right:
            mid = left + (right - left) / 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp < x:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res


