# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note: BFS
        """
        if not root:
            return 0
        queue = [root]
        min = 0

        while queue:
            min += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                # pop
                r = queue.pop(0)
                # process
                if not r.left and not r.right:
                    return min
                # generate and push
                if r.left: queue.append(r.left)
                if r.right: queue.append(r.right)
        return min

class SolutionV1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note: DFS
        """
        if not root:
            return 0
        self.min = float('inf')
        self.recur(root, 0)
        return self.min

    def recur(self, root, preLevel):
        if root is None:
                return
        if not root.left and not root.right and preLevel + 1 < self.min:
            self.min = preLevel + 1
            return
        self.recur(root.left, preLevel + 1)
        self.recur(root.right, preLevel + 1)


class SolutionV2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note: DFS
        """
        if not root:
            return 0
        minLeft = self.minDepth(root.left)
        minRight = self.minDepth(root.right)
        if minLeft == 0 or minRight == 0:
            return minLeft + minRight + 1
        else:
            return 1 + min(minLeft, minRight)
