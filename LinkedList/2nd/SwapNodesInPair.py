# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, res = ListNode(None), head.next
        first, second = head, head.next
        while first and second:
            pre.next, first.next, second.next = second, second.next, first
            if first.next:
                pre, first, second = first, first.next, first.next.next
            else:
                break
        return res


class SolutionV1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head
        res = pre
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return res.next



class SolutionV2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        a, b = head, head.next
        a.next, b.next = self.swapPairs(b.next), a
        return b


