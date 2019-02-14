class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        strsSorted = map(lambda s : "".join(sorted(s)), strs)
        #res = {}
        res = dict()
        for idx, s in enumerate(strsSorted):
            res.setdefault(s, []).append(strs[idx])
        return map(list, res.values())


class SolutionV1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        res = dict()
        for w in strs:
            mul = 1
            for c in w:
                mul *= prime[ord(c) - ord('a')]
            res.setdefault(mul, []).append(w)
        return map(list, res.values())
