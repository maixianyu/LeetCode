class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        sortedNums = sorted(nums)
        res = []
        for idxA, A in enumerate(sortedNums):
            if idxA > 0 and A == sortedNums[idxA-1]:
                continue
            idxB = idxA + 1
            while idxB < (len(sortedNums) - 2):
                B = sortedNums[idxB]
                if idxB > idxA + 1 and B == sortedNums[idxB-1]:
                    idxB += 1
                    continue
                idxC, idxD = idxB + 1, len(sortedNums) - 1
                while idxC < idxD:
                    cal = A + B + sortedNums[idxC] + sortedNums[idxD] - target
                    if cal < 0:
                        idxC += 1
                    elif cal > 0:
                        idxD -= 1
                    else:
                        res.append([A, B, sortedNums[idxC], sortedNums[idxD]])
                        idxC += 1
                        while sortedNums[idxC] == sortedNums[idxC - 1] and idxC < idxD:
                            idxC += 1
                        idxD -= 1
                        while sortedNums[idxD] == sortedNums[idxD + 1] and idxC < idxD:
                            idxD -= 1
                idxB += 1
        return res


class SolutionV1(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(l, r, result, N, localTarget):
            if r - l + 1 < N or N < 2 or numsSorted[l] * N > localTarget or numsSorted[r] * N < localTarget:
                return
            if N == 2:
                while l < r:
                    s = numsSorted[l] + numsSorted[r]
                    if s == localTarget:
                        results.append(result + [numsSorted[l], numsSorted[r]])
                        l += 1
                        r -= 1
                        while l < r and numsSorted[l] == numsSorted[l-1]:
                            l += 1
                        while l < r and numsSorted[r] == numsSorted[r+1]:
                            r -= 1
                    elif s < localTarget:
                        l += 1
                        while l < r and numsSorted[l] == numsSorted[l-1]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and numsSorted[r] == numsSorted[r+1]:
                            r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or i > l and numsSorted[i] != numsSorted[i-1]:
                        findNsum(i+1, r, result + [numsSorted[i]], N-1, localTarget - numsSorted[i])

        numsSorted = sorted(nums)
        results = []
        findNsum(0, len(numsSorted)-1, [], 4, target)
        return results


class SolutionV2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(l, r, result, N, localTarget):
            if r - l + 1 < N or N < 2 or numsSorted[l] * N > localTarget or numsSorted[r] * N < localTarget:
                return
            if N == 2:
                while l < r:
                    s = numsSorted[l] + numsSorted[r]
                    if s == localTarget:
                        results.append(result + [numsSorted[l], numsSorted[r]])
                        l += 1
                        while l < r and numsSorted[l] == numsSorted[l-1]:
                            l += 1
                    elif s < localTarget:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or i > l and numsSorted[i] != numsSorted[i-1]:
                        findNsum(i+1, r, result + [numsSorted[i]], N-1, localTarget - numsSorted[i])

        numsSorted = sorted(nums)
        results = []
        findNsum(0, len(numsSorted)-1, [], 4, target)
        return results
