class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        lenN = len(nums)
        res = []
        tupleSet = set()

        snums = sorted(nums)
        for idxA, A in enumerate(snums):
            haveB = set()
            idxB = idxA + 1
            if idxA > 0 and A == snums[idxA-1]:
                continue
            while idxB < lenN:
                B = snums[idxB]
                needed = - A - B
                if needed in haveB and (A, needed, B) not in tupleSet:
                    res.append([A, needed, B])
                    tupleSet.add((A, needed, B))
                haveB.add(B)
                idxB += 1

        return res



class SolutionV1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        lenN = len(nums)
        res = set()

        snums = sorted(nums)
        for idxA, A in enumerate(snums):
            haveB = set()
            idxB = idxA + 1
            if idxA > 0 and A == snums[idxA-1]:
                continue
            while idxB < lenN:
                B = snums[idxB]
                needed = - A - B
                if needed in haveB:
                    res.add((A, needed, B))
                else:
                    haveB.add(B)
                idxB += 1

        return map(list, res)



class SolutionV2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        lenN = len(nums)
        res = set()

        snums = sorted(nums)
        for idxA, A in enumerate(snums[:-2]):
            if idxA > 0 and A == snums[idxA-1]:
                continue
            idxB, idxC = idxA + 1, lenN - 1
            while idxB < idxC:
                sumup = A + snums[idxB] + snums[idxC]
                if sumup < 0:
                    idxB += 1
                elif sumup > 0:
                    idxC -= 1
                else:
                    res.add((A, snums[idxB], snums[idxC]))
                    idxB += 1
                    idxC -= 1

        return map(list, res)
