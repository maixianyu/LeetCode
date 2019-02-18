class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        if not commands:
            return 0

        direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        deltaD = [1, -1]
        DIdx = 0
        x, y = 0, 0
        res = 0

        for c in commands:
            if c in (-1, -2):
                DIdx += deltaD[c]
            else:
                targetX, targetY = x + direct[DIdx % 4][0] * c, y + direct[DIdx % 4][1] * c
                if direct[DIdx % 4][0]:
                    for xMoving in range(x + direct[DIdx % 4][0], targetX, direct[DIdx % 4][0]):
                        if [xMoving, y] in obstacles:
                            targetX = xMoving - direct[DIdx % 4][0]
                            break
                    x = targetX
                #elif direct[DIdx % 4][1]:
                else:
                    for yMoving in range(y + direct[DIdx % 4][1], targetY, direct[DIdx % 4][1]):
                        if [x, yMoving] in obstacles:
                            targetY = yMoving - direct[DIdx % 4][1]
                            break
                    y = targetY
            res = max(res, x * x + y * y)
        return res

class SolutionV1(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        if not commands:
            return 0

        direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        DIdx = 0
        x, y = 0, 0
        res = 0
        oSet = set(map(tuple, obstacles))

        for c in commands:
            if c == -1:
                DIdx = (DIdx - 1) % 4
            elif c == -2:
                DIdx = (DIdx + 1) % 4
            else:
                deltaX, deltaY = direct[DIdx % 4]
                while c and (x + deltaX, y + deltaY) not in oSet:
                    x, y = x + deltaX, y + deltaY
                    c -= 1
            res = max(res, x * x + y * y)
        return res




