class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        qCur = []
        qTmp = [root]

        while qCur or qTmp:
            if not qCur:
                qCur = qTmp[:]
                qTmp = []
                res += 1
            node = qCur.pop()
            if node.left: qTmp.append(node.left)
            if node.right: qTmp.append(node.right)
        return res


class SolutionV1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = 0
        self.helper(root, 0)
        return self.res

    def helper(self, root, depth):
        if not root:
            self.res = max(self.res, depth)
            return
        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)


from collections import deque
class SolutionV2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        nStack = deque([root])
        vStack = deque([1])
        visited = set()

        while nStack:
            root = nStack.pop()
            val  = vStack.pop()
            visited.add(root)
            res = max(res, val)
            if root.right and root.right not in visited:
                nStack.append(root.right)
                vStack.append(val + 1)
            if root.left and root.left not in visited:
                nStack.append(root.left)
                vStack.append(val + 1)
        return res




