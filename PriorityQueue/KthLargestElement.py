from heapq import *
class KthLargestV1(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.count = 0
        self.maxCount = k
        self.heap = []
        for i in nums:
            if self.count == k:
                if i > self.heap[0]:
                    heapreplace(self.heap, i)
                continue
            heappush(self.heap, i)
            self.count += 1


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.count < self.maxCount:
            heappush(self.heap, val)
            self.count += 1
        else:
            if (val > self.heap[0]):
                heappop(self.heap)
                heappush(self.heap, val)
        res = self.heap[0]
        return res

class KthLargestV2(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.count = 0
        self.maxCount = k
        self.heap = nums[:]
        heapify(self.heap)
        self.numsLength = len(nums)
        if self.numsLength > k:
            self.count = k
            for i in range(self.numsLength - k):
                heappop(self.heap)
        else:
            self.count = self.numsLength

        print(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.count < self.maxCount:
            heappush(self.heap, val)
            self.count += 1
        else:
            if (val > self.heap[0]):
                heapreplace(self.heap, val)
        res = self.heap[0]
        return res

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)