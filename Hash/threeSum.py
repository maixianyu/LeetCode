class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        if lenNums < 3:
            return []
        nums.sort()
        res = set()
        for idxA, a in enumerate(nums[:-2]):
            if idxA >= 1 and nums[idxA] == nums[idxA-1]:
                continue
            need = set()
            for idxB, b in enumerate(nums[(idxA+1):]):
                if b in need:
                    res.add((a, -a-b, b))
                else:
                    need.add(-a-b)
        return map(list, res)

    def threeSumV1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        if lenNums < 3:
            return []
        nums.sort()
        res = set()

        for idxA, a in enumerate(nums[:-2]):
            if idxA >= 1 and a == nums[idxA - 1]:
                continue
            idxB = idxA + 1
            idxC = lenNums - 1
            while idxB < idxC:
                b, c = nums[idxB], nums[idxC]
                sum = a + b + c
                if sum < 0:
                    idxB += 1
                elif sum > 0:
                    idxC -= 1
                else:
                    res.add((a, b, c))
                    idxB += 1
                    idxC -= 1
                    while nums[idxB] == b and idxB < idxC:
                        idxB += 1
                    while nums[idxC] == c and idxB < idxC:
                        idxC -= 1
        return map(list, res)


