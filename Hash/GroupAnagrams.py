class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortStrs = map(sorted, strs)
        sortStrs = map(''.join, sortStrs)
        groupDict = dict()
        for idx, s in enumerate(strs):
            if sortStrs[idx] not in groupDict:
                groupDict[sortStrs[idx]] = [s]
            else:
                groupDict[sortStrs[idx]].append(s)
        return list(groupDict.values())
