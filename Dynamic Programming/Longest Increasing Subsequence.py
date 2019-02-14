class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = []
        res = 0
        for idx, ele in enumerate(nums):
            maxprev = 0
            for j in range(idx):
                if dp[j] > maxprev and ele > nums[j]:
                    maxprev = dp[j]
            dp.append(maxprev+1)
            res = max(res, dp[-1])
        return res

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lis = []
        for ele in nums:
            if lis:
                if ele > lis[-1]:
                    lis.append(ele)
                else:
                    idxF = self._search(lis, ele)
                    if idxF > len(lis):
                        lis.append(ele)
                    else:
                        lis[idxF] = ele
            else:
                lis.append(ele)
        return len(lis)

    def _search(self, lis, ele):
        left, right = 0, len(lis) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if lis[mid] == ele:
                return mid
            elif lis[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1
        return left


