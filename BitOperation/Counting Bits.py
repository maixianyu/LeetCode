class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = [0]
        idx = 1
        while idx < num + 1:
            count.append(count[idx & (idx - 1)] + 1)
            idx += 1
        return count