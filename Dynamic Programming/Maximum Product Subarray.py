class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = max(nums)
        prod = [nums]
        for _ in range(len(nums) - 1):
            prod.append([])
            curL = len(prod) - 1
            for i in range(len(prod[-2])-1):
                v = prod[-2][i] * nums[i + curL]
                res = max(v, res)
                prod[-1].append(v)
        return res


class SolutionV1(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [[0] * 2 for _ in range(2)]
        dp[0], dp[1] = [nums[0], nums[0]], [nums[0], nums[0]]
        res = nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, i % 2 - 1
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])
        return res

