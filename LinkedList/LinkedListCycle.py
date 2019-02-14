# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pFast, pSlow = head, head
        while pSlow and pFast and pFast.next:
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pFast is pSlow:
            #if pFast == pSlow:
                return True
        return False

