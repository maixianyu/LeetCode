class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        lenNums = len(nums)
        if lenNums < k:
            return [max(nums)]
        dq = []
        res = []
        idx = 0
        while idx < lenNums:
            if idx >= k:
                res.append(dq[0])
            if len(dq) == k:
                dq.pop(0)
            while dq and dq[-1] < nums[idx]:
                dq.pop()
            dq.append(nums[idx])
            idx += 1
        res.append(dq[0])
        return res

class SolutionV2(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        window = []
        res = []
        for i, x in enumerate(nums):
            if i >= k and i - window[0] >= k:
                window.pop(0)
            while window and x > nums[window[-1]]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

import collections
class SolutionV3(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        window = collections.deque()
        res = []
        for i, x in enumerate(nums):
            if i >= k and i - window[0] >= k:
                window.popleft()
            while window and x > nums[window[-1]]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


sol = SolutionV2()
# test
res = sol.maxSlidingWindow([2, 4, 22, 11, 25, 6], 2)
print(res)

res = sol.maxSlidingWindow([2, 4, 22, 11, 25, 6], 1)
print(res)

res = sol.maxSlidingWindow([2, 4, 22, 11, 25, 6], 10)
print(res)
