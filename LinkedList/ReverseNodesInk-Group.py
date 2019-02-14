# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroupV1(self, head, k):
        """ very very terrible code. complicated and doesnt work at all """
        prev, prev.next, cur = self, head, head
        tailGroup = headGroup = None
        count = k

        # traverse list
        while cur:
            #reverse group
            tailGroup = cur
            while count > 0:
                print("cur=" + str(cur.val))
                nextTmp = cur.next
                cur.next = headGroup
                headGroup = cur
                cur = nextTmp
                count = count - 1

                if cur is None:
                    while headGroup:
                        nextTmp = headGroup.next
                        headGroup.next = cur
                        cur = headGroup
                        headGroup = nextTmp
                    prev.next = cur
                    return self.next

            # reset
            count = k
            prev.next = headGroup
            prev = tailGroup
            headGroup, tailGroup = None, None
        return self.next


    def reverseKGroupV2(self, head, k):
        prev, prev.next = self, head
        left, right, connect = head, head, prev
        if head:
            remaining = True
        else:
            return None
        while remaining:
            count = 0
            while right:
                count += 1
                right = right.next
                if count == k:
                    cur = left
                    for i in range(k):
                        cur.next, cur, prev = prev, cur.next, cur
                    break
                elif right is None:
                    return self.next

            if right is None:
                remaining = False
            # full and reverse
            connect.next, connect = prev, left
            left.next, left = right, right
        return self.next

    def reverseKGroupV3(self, head, k):
        prev, prev.next = self, head
        left, right, connect = head, head, prev
        while True:
            count = 0
            while right and count < k:
                count += 1
                right = right.next
            if count == k:
                cur, prev = left, right
                for i in range(k):
                    cur.next, cur, prev = prev, cur.next, cur
                connect.next, connect, left.next, left = prev, left, right, right
            else:
                return self.next

    def reverseKGroup(self, head, k):
        # detect length
        cur = head
        count = 0
        while cur and count < k:
            cur = cur.next
            count += 1
        # judge
        if count < k:
            return head
        else:
            reNode = self.reverseKGroup(cur, k)
            prev, prev.next, cur = ListNode(None), head, head
            for i in range(k):
                cur.next, prev, cur = prev, cur, cur.next
            head.next = reNode
            return prev







