class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        count = {}
        maxCount = 0
        maxNum = 0
        for i in nums:
            count[i] = count.setdefault(i, 0) + 1
            if count[i] > maxCount:
                maxNum = i
                maxCount = count[i]
        return maxNum


class SolutionV1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        res, resCount = nums[0], 1
        for i in nums[1:]:
            if resCount == 0:
                res = i
            if i == res:
                resCount += 1
            else:
                resCount -= 1
        return res

class SolutionV2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        mask = 1
        major = 0

        for i in range(32):
            mCount = 0
            for ele in nums:
                if ele & mask:
                    mCount += 1
                if mCount > N / 2:
                    if i == 31:
                        major = -((1<<31)-major)
                        break
                    else:
                        major |= mask
                        break
            mask <<= 1

        return major

