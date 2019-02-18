class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return True
        left = [0] * 3
        cvalue = [5, 10, 20]

        for b in bills:
            remaining = b - cvalue[0]
            # enumerate or dict
            for idx, p in enumerate(cvalue):
                if b == p:
                    left[idx] += 1
                    break

            # change
            if remaining:
                j = len(left) - 2
                for idx in range(j, -1, -1):
                    while left[idx] and remaining - cvalue[idx] >= 0:
                        remaining -= cvalue[idx]
                        left[idx] -= 1
                if remaining:
                    return False

        return True

class SolutionV1(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return True
        left = {5:0, 10:0, 20:0}
        cvalue = [5, 10, 20]

        for b in bills:
            remaining = b - cvalue[0]
            # enumerate or dict
            left[b] += 1

            # change
            if remaining:
                j = len(cvalue) - 2
                for idx in range(j, -1, -1):
                    while left[cvalue[idx]] and remaining - cvalue[idx] >= 0:
                        remaining -= cvalue[idx]
                        left[cvalue[idx]] -= 1
                if remaining:
                    return False

        return True


class SolutionV2(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return False
        five, ten, twenty = 0, 0, 0
        for b in bills:
            if b == twenty:
                twenty += 1
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            elif b == ten:
                ten += 1
                five -= 1
            else:
                five += 1

            if five < 0:
                return False
        return True


class SolutionV3(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return False
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                five -= 1
            elif ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3

            if five < 0:
                return False
        return True
