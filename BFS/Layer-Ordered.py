# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        curLayer = []
        curLayerIdx = 0
        stack = []
        stack.append((0, root))

        while stack:
            layerIdx, root = stack.pop(0)

            # process node
            if not curLayer:
                curLayer.append(root.val)
            else:
                if curLayerIdx != layerIdx:
                    res.append(curLayer)
                    curLayerIdx = layerIdx
                    curLayer = [root.val]
                else:
                    curLayer.append(root.val)

            # get children and add to stack
            if root.left:
                stack.append((layerIdx+1, root.left))
            if root.right:
                stack.append((layerIdx+1, root.right))
        res.append(curLayer)
        return res



class SolutionV1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        curLayer = []
        stack = [root]
        stackTmp = []

        while stack or stackTmp:
            if not stack:
                res.append(curLayer)
                stack = stackTmp
                stackTmp, curLayer = [], []

            root = stack.pop(0)

            # process node
            curLayer.append(root.val)

            # get children and add to stack
            if root.left:
                stackTmp.append(root.left)
            if root.right:
                stackTmp.append(root.right)

        res.append(curLayer)
        return res

class SolutionV2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :n: Batch Processing
        """
        if root is None:
            return []

        res = []
        stack = []
        stack.append(root)

        while stack:
            curLayer = []
            stackTmp = []
            for r in stack:
                curLayer.append(r.val)
                if r.left: stackTmp.append(r.left)
                if r.right: stackTmp.append(r.right)
            res.append(curLayer)
            stack = stackTmp

        return res

class SolutionV3(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :n: Batch Processing (Better Version)
        """
        if root is None:
            return []

        res = []
        stack = []
        stack.append(root)

        while stack:
            curLayer = []
            levelSize = len(stack)
            for _ in range(levelSize):
                r = stack.pop(0)
                curLayer.append(r.val)
                if r.left: stack.append(r.left)
                if r.right: stack.append(r.right)
            res.append(curLayer)

        return res

class SolutionV4(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :note: DFS
        """
        if root is None:
            return []
        res = []
        self._recur(root, res, 0)
        return res

    def _recur(self, root, res, level):
        if not root:
            return
        if level >= len(res):
            res.append([root.val])
        else:
            res[level].append(root.val)
        self._recur(root.left, res, level+1)
        self._recur(root.right, res, level+1)


