# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head
        pre, pre.next, cur = ListNode(None), head, head
        self.pre = pre
        while cur:
            # detect K length
            tmp = pre
            for i in range(k):
                tmp = tmp.next
                if not tmp:
                    return self.pre.next

            # reverse
            tmpCur = cur
            tmpPre = pre
            for i in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            tmpCur.next = cur
            tmpPre.next = pre
            pre = tmpCur

        return self.pre.next

class SolutionV1(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre, cur = None, head

        # detect
        tmp = head
        for _ in range(k):
            if not tmp:
                return head
            tmp = tmp.next

        # reverse
        for _ in range(k):
            cur.next, pre, cur = pre, cur, cur.next
        head.next = self.reverseKGroup(cur, k)
        return pre

class SolutionV2(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # detect
        tmp = head
        count = 0
        while tmp and count < k:
            tmp = tmp.next
            count += 1

        if count == k:
            # reverse
            pre, cur = None, head
            for _ in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            head.next = self.reverseKGroup(cur, k)
            return pre
        else:
            return head



