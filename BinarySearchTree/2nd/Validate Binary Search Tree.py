# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.comp = float("-inf")
        return self.midTraverse(root)

    def midTraverse(self, root):
        if not root:
            return True

        if not self.midTraverse(root.left):
            return False

        if root.val > self.comp:
            self.comp = root.val
        else:
            return False

        return self.midTraverse(root.right)


class SolutionV1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nlist = []
        self.midTraverse(root, nlist)
        for idx in range(1, len(nlist)):
            if nlist[idx] < nlist[idx-1]:
                return False
        return True

    def midTraverse(self, root, nodeList):
        if not root:
            return
        self.midTraverse(root.left, nodeList)
        nodeList.append(root.val)
        self.midTraverse(root.right, nodeList)

class SolutionV2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        prev = None
        nlist = []

        while nlist or root:
            while root:
                nlist.append(root)
                root = root.left
            root = nlist.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right

        return True


class SolutionV3(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minNum = float("-inf")
        maxNum = float("inf")
        return self.comp(root, minNum, maxNum)

    def comp(self, root, minNum, maxNum):
        if not root:
            return True
        if root.val <= minNum or root.val >= maxNum:
            return False
        return self.comp(root.left, minNum, root.val) & self.comp(root.right, root.val, maxNum)

