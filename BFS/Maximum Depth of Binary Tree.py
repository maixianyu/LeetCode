# Definition for a binary tree node.
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
        :note: BFS
        """
        if not root:
            return 0
        queue = [root]
        maxDepth = 0

        while queue:
            levelSize = len(queue)
            maxDepth += 1
            for _ in range(levelSize):
                r = queue.pop(0)
                if r.left: queue.append(r.left)
                if r.right: queue.append(r.right)

        return maxDepth


class SolutionV1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note: DFS
        """
        maxDepth = self._recur(root, 0)
        return maxDepth

    def _recur(self, root, preLevel):
        if root is None:
            return preLevel

        dLeft = self._recur(root.left, preLevel+1)
        dRight = self._recur(root.right, preLevel+1)
        return max(dLeft, dRight)

class SolutionV2(object):
    def maxDepth(self, root):
        if not root:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        return 1 + max(maxLeft, maxRight)
