class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (len(s) == 0) ^ (len(t) == 0):
            return False

        tMap = dict()
        for ele in t:
            if ele in tMap:
                tMap[ele] = tMap[ele] + 1
            else:
                tMap[ele] = 1

        for ele in s:
            if ele in tMap and tMap[ele] >= 1:
                tMap[ele] = tMap[ele] - 1
            else:
                return False

        for ele in t:
            if tMap[ele] != 0:
                return False
        return True

    def isAnagramV1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = dict()
        tMap = dict()
        for ele in t:
            tMap[ele] = tMap.get(ele, 0) + 1

        for ele in s:
            sMap[ele] = sMap.get(ele, 0) + 1

        return sMap == tMap

    def isAnagramV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


