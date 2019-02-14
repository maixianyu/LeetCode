class Solution(object):
    def compListVal(self, _list, _idx, _nums):
        length = len(_list)
        if _list and _nums[_idx] > _list[0]:
            while _list:
                _list.pop()
        elif length > 1:
            while _list[-1] < _nums[_idx]:
                _list.pop()
        _list.append(_nums[_idx])

    def maxSlidingWindow(self, nums, k):
        inputLen = len(nums)
        if k < 1 or k > inputLen:
            return []

        dequeue, maxList = [], []
        for eleIdx in range(len(nums)):
            if eleIdx >= k and nums[eleIdx-k] == dequeue[0]:
                dequeue = dequeue[1:]
            self.compListVal(dequeue, eleIdx, nums)
            if eleIdx >= (k - 1):
                maxList.append(dequeue[0])
        print(maxList)
        return maxList

class SolutionV2(object):
    def maxSlidingWindow(self, nums, k):
        inputLen = len(nums)
        if k < 1 or k > inputLen:
            return []

        dequeue, maxList = [], []
        for eleIdx, ele in enumerate(nums):
            if eleIdx >= k and eleIdx - k >= dequeue[0]:
                dequeue.pop(0)
            while dequeue and nums[dequeue[-1]] <= ele:
                dequeue.pop()
            dequeue.append(eleIdx)
            if eleIdx >= (k - 1):
                maxList.append(nums[dequeue[0]])
        print(maxList)
        return maxList

