class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        if lenNums < 4:
            return []
        res = set()
        nums.sort()

        for idxA, a in enumerate(nums[:-3]):
            if idxA >= 1 and a == nums[idxA-1]:
                continue
            for idxB in range(idxA+1, lenNums-2):
                b = nums[idxB]
                if idxB >= idxA+2 and b == nums[idxB-1]:
                    continue
                need = set()
                for idxC in range(idxB+1, lenNums):
                    c = nums[idxC]
                    if c not in need:
                        need.add(target-a-b-c)
                    else:
                        res.add((a, b, target-a-b-c, c))
                        print(str(idxA) + "," + str(idxB) + "," + str(idxC))
        return map(list, res)

    def fourSumV1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        if lenNums < 4:
            return []

        res = []
        nums.sort()
        for idxA, a in enumerate(nums[:-3]):
            if idxA >= 1 and a == nums[idxA-1]:
                continue
            for idxB in range(idxA+1, lenNums - 2):
                b = nums[idxB]
                if idxB >= idxA+2 and b == nums[idxB-1]:
                    continue
                idxC, idxD = idxB + 1, lenNums - 1
                while idxC < idxD:
                    c, d = nums[idxC], nums[idxD]
                    sum = a + b + c + d - target
                    if sum < 0:
                        idxC += 1
                        continue
                    elif sum > 0:
                        idxD -= 1
                        continue
                    else:
                        res.append([a, b, c, d])
                        idxC += 1
                        idxD -= 1
                        while nums[idxC] == c and idxC < idxD:
                            idxC += 1
                        while nums[idxD] == d and idxC < idxD:
                            idxD -= 1
        return res




