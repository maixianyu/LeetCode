class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}

        for idx, i in enumerate(nums):
            m[i] = idx

        for idx, i in enumerate(nums):
            another = target - i
            if another in m and m[another] > idx:
                return [idx, m[another]]
        return []

class SolutionV1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        have = {}

        for idx, i in enumerate(nums):
            needed = target - i
            if needed in have:
                return [have[needed], idx]
            have[i] = idx
        return []
