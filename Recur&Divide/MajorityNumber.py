class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = dict()
        maxNum = None
        for ele in nums:
            if ele not in numMap:
                numMap[ele] = 1
            else:
                numMap[ele] += 1
            if maxNum is None or numMap[ele] > numMap[maxNum]:
                maxNum = ele
        return maxNum

class SolutionV1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenN = len(nums)
        nums = sorted(nums)
        return nums[lenN / 2]
