# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        def getListNodeLength(head):
            n = 0
            while head:
                n += 1
                head = head.next
            return n
        def moveStep(head, n):
            while n > 0:
                head = head.next
                n -= 1
            return head
        lenA = getListNodeLength(headA)
        lenB = getListNodeLength(headB)
        if lenA > lenB:
            diff = lenA - lenB
            headA = moveStep(headA, diff)
        elif lenA < lenB:
            diff = lenB - lenA
            headB = moveStep(headB, diff)
        while headA and headB:
            if headA.val == headB.val:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(2)
    b1 = ListNode(3)
    b2 = ListNode(4)
    b3 = ListNode(5)
    c1 = ListNode(6)
    c2 = ListNode(7)
    c3 = ListNode(8)

    headA = a1
    a1.next = a2
    a2.next = c1
    headB = b1
    b1.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = c3

    s = Solution()
    node = s.getIntersectionNode(headA, headB)
    print node.val
