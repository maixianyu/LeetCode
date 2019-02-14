# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reLength = 0
        count1 = count2 = 0
        pSlow = pFast = head
        while pSlow and pFast and pFast.next:
            pSlow = pSlow.next
            pFast = pFast.next.next
            count1 = count1 + 1
            count2 = count2 + 2
            if pSlow is pFast:
                cycleLength = count2 - count1
                reLength = count1 - cycleLength
                break

        if (pFast == None) or (pFast.next == None):
            return None

        pSlow = head
        while reLength != 0:
            pSlow = pSlow.next
            reLength = reLength - 1

        while pSlow and pFast and (pSlow is not pFast):
            pSlow = pSlow.next
            pFast = pFast.next
        return pSlow

    def detectCycleRebuild(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pSlow = pFast = head
        while pSlow and pFast and pFast.next:
            pSlow, pFast = pSlow.next, pFast.next.next
            if pSlow is pFast:
                pSlow = head
                while pSlow != pFast:
                    pSlow, pFast = pSlow.next, pFast.next
                return pSlow
        return None
