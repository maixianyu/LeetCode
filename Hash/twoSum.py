class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        eleMap = dict()
        for ele in nums:
            eleMap[ele] = list()
        for idx, ele in enumerate(nums):
            eleMap[ele].append(idx)
        for idx, ele in enumerate(nums):
            if (target - ele) in eleMap.keys():
                for palIdx in eleMap[target - ele]:
                    if idx != palIdx:
                        return [idx, palIdx]
        return []


    def twoSumV1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        eleMap = dict()
        for idx, ele in enumerate(nums):
            pal = (target - ele)
            if pal in eleMap.keys():
                return [idx, eleMap[pal]]
            else:
                eleMap[ele] = idx
        return []



