# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        visited = set()
        qCur = []
        qTmp = [root]
        vTmp = [root.val]
        res = []

        while qCur or qTmp:
            if not qCur:
                qCur = qTmp[:]
                res.append(vTmp[:])
                qTmp = []
                vTmp = []

            node = qCur.pop(0)
            visited.add(node)

            if node.left and node.left not in visited:
                qTmp.append(node.left)
                vTmp.append(node.left.val)
            if node.right and node.right not in visited:
                qTmp.append(node.right)
                vTmp.append(node.right.val)

        return res

class SolutionV1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        visited = set()
        self.dfs(root, res, visited, 0)
        return res

    def dfs(self, root, res, visited, depth):
        if not root:
            return
        if depth >= len(res):
            res.append([])

        res[depth].append(root.val)
        visited.add(root)

        if root.left and root.left not in visited:
            self.dfs(root.left, res, visited, depth + 1)
        if root.right and root.right not in visited:
            self.dfs(root.right, res, visited, depth + 1)


class SolutionV2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []

