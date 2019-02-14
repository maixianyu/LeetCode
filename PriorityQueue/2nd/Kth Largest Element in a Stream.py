class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        N = len(nums)
        self.heap = [0]
        self.k = k
        if N > k:
            self.heap.extend(nums[:k])
        else:
            self.heap.extend(nums[:])

        # heapify
        self.heapify()

        # add
        if N > k:
            for i in range(N - k):
                self.add(nums[k+i])

    def heapify(self):
        amount = len(self.heap)
        idx = int(amount / 2)
        while idx >= 1:
            self.shiftDown(self.heap, idx, amount)
            idx -= 1

    def shiftDown(self, heap, idx, amount):
        min = idx
        if idx * 2 < amount and heap[min] > heap[idx * 2]:
            min = idx * 2
        if idx * 2 + 1 < amount and heap[min] > heap[idx * 2 + 1]:
            min = idx * 2 + 1
        if min != idx:
            heap[idx], heap[min] = heap[min], heap[idx]
            self.shiftDown(heap, min, amount)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        amount = len(self.heap)
        if amount - 1 < self.k:
            self.heap.append(val)
            self.heapify()
        else:
            if val > self.heap[1]:
                self.heap[1] = val
                self.shiftDown(self.heap, 1, amount)
        return self.heap[1]

from heapq import *
class KthLargestV2(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums[:]
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heapreplace(self.heap, val)
        return self.heap[0]


