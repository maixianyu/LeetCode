# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        qCur = []
        qTmp = [root]
        depth = 0
        visited = set()

        while qCur or qTmp:
            if not qCur:
                qCur = qTmp[:]
                qTmp = []
                depth += 1

            node = qCur.pop()
            if not node.left and not node.right:
                return depth
            if node.left and node.left not in visited:
                visited.add(node.left)
                qTmp.append(node.left)
            if node.right and node.right not in visited:
                visited.add(node.right)
                qTmp.append(node.right)
        return depth



class SolutionV1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float("+inf")
        self.helper(root, 1)
        return self.res

    def helper(self, root, depth):
        if not root:
            return
        if not root.left and not root.right:
            self.res = min(self.res, depth)
            return
        if root.left: self.helper(root.left, depth + 1)
        if root.right: self.helper(root.right, depth + 1)



class SolutionV2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + (min(left, right) or max(left, right))
