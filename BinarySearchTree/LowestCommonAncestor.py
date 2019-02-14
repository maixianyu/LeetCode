# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPorQ(root, pp, qq):
            if root is None:
                return None, None
            pqLeft, resLeft = findPorQ(root.left, pp, qq)
            pqRight, resRight = findPorQ(root.right, pp, qq)
            if resLeft:
                return None, resLeft
            if resRight:
                return None, resRight
            pqList = []
            pq = None
            if root.val == pp.val or root.val == qq.val:
                pqList.append(root)
                pq = root
            if pqLeft:
                pqList.append(pqLeft)
                pq = pqLeft
            if pqRight:
                pqList.append(pqRight)
                pq = pqRight
            if len(pqList) == 2:
                return None, root
            return pq, None

        pq, res = findPorQ(root, p, q)
        return res

class SolutionV1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPorQ(root, pp, qq):
            if root is None:
                return None
            resLeft = findPorQ(root.left, pp, qq)
            resRight = findPorQ(root.right, pp, qq)
            pqCount = 0

            pq = None
            if resLeft:
                if resLeft.val != pp.val and resLeft.val != qq.val:
                    return resLeft
                pq = resLeft
                pqCount += 1

            if resRight:
                if resRight.val != pp.val and resRight.val != qq.val:
                    return resRight
                pq = resRight
                pqCount += 1

            if root.val == pp.val or root.val == qq.val:
                pq = root
                pqCount += 1
            if pqCount == 2:
                return root
            return pq

        res = findPorQ(root, p, q)
        return res

class SolutionV2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPorQ(root, pp, qq):
            if root is None:
                return None
            if root.val == pp.val or root.val == qq.val:
                return root

            resLeft = findPorQ(root.left, pp, qq)
            resRight = findPorQ(root.right, pp, qq)
            pqCount = 0

            pq = None
            for res in [resLeft, resRight]:
                if res:
                    pq = res
                    pqCount += 1

            if pq and pq.val != pp.val and pq.val != qq.val:
                return pq

            if pqCount == 2:
                return root

            return pq

        res = findPorQ(root, p, q)
        return res

class SolutionV3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None
