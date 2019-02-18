class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0

        gSort = sorted(g)
        sSort = sorted(s)

        gIdx = 0
        res = 0
        for sz in sSort:
            if gIdx < len(gSort) and sz >= gSort[gIdx]:
                gIdx += 1
                res += 1
        return res
