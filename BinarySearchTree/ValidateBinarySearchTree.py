# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionV1(object):
    def treeSort(self, root):
        if root is None:
            return []
        left = self.treeSort(root.left)
        right = self.treeSort(root.right)
        return left + [root.val] + right

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sortVals = self.treeSort(root)
        for idx, ele in enumerate(sortVals):
            if idx >= 1 and ele <= sortVals[idx-1]:
                return False
        return True


class SolutionV2(object):
    """not working"""
    def recur(self, root, side):
        if root is None:
            return True, None
        boolLeft, valLeft = self.recur(root.left, False)
        boolRight, valRight = self.recur(root.right, True)
        if boolLeft & boolRight == False:
            return False, None
        if side:
            if valLeft:
                v = valLeft
            else:
                v = root.val
        else:
            if valRight:
                v = valRight
            else:
                v = root.val

        if valLeft and valRight:
            return root.val < valRight and root.val > valLeft, v
        elif valRight:
            return root.val < valRight, v
        elif valLeft:
            return root.val > valLeft, v
        else:
            return True, v

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        boolRes, v = self.recur(root, False)
        return boolRes

class SolutionV3(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)


class SolutionV3(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)

    def isValid(self, root, min, max):
        if root is None:
            return True
        if min and root.val <= min:
            return False
        if max and root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)


class SolutionV4(object):
    """None is not necessary. Use float inf"""
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))

    def check_bst(self, node, left, right):
        if not node:
            return True

        if not left < node.val < right:
            return False

        return (self.check_bst(node.left, left, node.val)
                and self.check_bst(node.right, node.val, right))

class SolutionV5(object):
    """Binary Tree, in-order traversal, use Stack, but O(2N)"""
    def isValidBST(self, root):
        if root is None:
            return True
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True
