class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
