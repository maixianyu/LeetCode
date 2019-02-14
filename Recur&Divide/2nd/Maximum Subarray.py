class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        N = len(nums)
        sum = [0 for _ in range(N)]
        sum[0] = nums[0]
        res = sum[0]

        for i in range(1, N):
            sum[i] = nums[i] + max(sum[i-1], 0)
            if sum[i] > res:
                res = sum[i]

        return res


class SolutionV1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        N = len(nums)
        sumLeft1, sumRight1, sumSub1 = self.half(nums[0:N/2])
        sumLeft2, sumRight2, sumSub2 = self.half(nums[N/2:])
        return max(sumSub1, sumSub2, sumRight1 + sumLeft2)

    def half(self, nums):
        if not nums:
            return float("-inf"), float("-inf"), float("-inf")
        if len(nums) == 1:
            return nums[0], nums[0], nums[0]

        sumLeft, sumRight, sumSub = 0, 0, 0
        sumLeftTemp, sumLeft = 0, nums[0]
        for i in nums:
            sumLeftTemp += i
            if sumLeftTemp > sumLeft:
                sumLeft = sumLeftTemp

        sumRightTemp, sumRight = 0, nums[-1]
        for i in range(len(nums)-1, -1, -1):
            sumRightTemp += nums[i]
            if sumRightTemp > sumRight:
                sumRight = sumRightTemp

        sumSub = self.maxSubArray(nums)
        return sumLeft, sumRight, sumSub


class SolutionV2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        N = len(nums)
        sumLeft, sumRight, sumWhole, sumSub = self.half(nums)
        return max(sumSub, sumWhole)

    def half(self, nums):
        if not nums:
            return float("-inf"), float("-inf"), float("-inf"), float("-inf")
        if len(nums) == 1:
            return nums[0], nums[0], nums[0], nums[0]

        N = len(nums)
        t1 = self.half(nums[0:N/2])
        t2 = self.half(nums[N/2:])
        sumLeft = max(t1[0], t1[2] + t2[0])
        sumRight = max(t2[1], t1[1] + t2[2])
        sumWhole = sum(nums)
        sumSub = max(t1[1] + t2[0], max(t1[3], t2[3]))
        return sumLeft, sumRight, sumWhole, sumSub

