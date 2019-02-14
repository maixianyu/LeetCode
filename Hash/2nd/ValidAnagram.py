class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class SolutionV1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = dict()
        tMap = dict()
        for c in s:
            sMap[c] = sMap.setdefault(c, 0) + 1
        for c in t:
            tMap[c] = tMap.setdefault(c, 0) + 1
        return sMap == tMap


class SolutionV2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = [0] * 26
        tMap = [0] * 26

        for c in s:
            sMap[ord(c) - ord('a')] += 1
        for c in t:
            tMap[ord(c) - ord('a')] += 1

        return sMap == tMap

class SolutionV3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = [0] * 26
        tMap = [0] * 26

        for c in s:
            sMap[ord(c) - ord('a')] += 1
        for c in t:
            if sMap[ord(c) - ord('a')] == 0:
                return False
            tMap[ord(c) - ord('a')] += 1

        return sMap == tMap


