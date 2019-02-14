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
        if not head:
            return head

        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break

        if not slow.next or not fast.next or not fast.next.next:
            return None

        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next

        return slow

class SolutionV1(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow, fast = slow.next, fast.next.next
        except:
            return None

        slow = head
        fast = fast.next
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow



