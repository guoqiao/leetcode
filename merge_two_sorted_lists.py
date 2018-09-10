#!/usr/bin/env python

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_val(self):
        if self.next:
            print(self.val, end=' ')
            self.next.print_val()
        else:
            print(self.val)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = tail = ListNode(None)
        while (l1 and l2):
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return head.next


def to_list(node):
    lst = []
    while (node != None):
        lst.append(node.val)
        node = node.next
    return lst


def from_list(lst):
    head = tail = ListNode(None)
    for val in lst or []:
        tail.next = ListNode(val)
        tail = tail.next
    return head.next


if __name__ == '__main__':
    items = [
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1, 2], [], [1, 2]),
        ([], [1, 2], [1, 2]),
        ([1], [1], [1, 1]),
        ([1, 2], [1], [1, 1, 2]),
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([1, 2, 4], [], [1, 2, 4]),
        ([1, 2, 4], [0], [0, 1, 2, 4]),
    ]
    s = Solution()
    for l1, l2, l3 in items:
        print(l1, l2, l3)
        assert to_list(s.mergeTwoLists(from_list(l1), from_list(l2))) == l3
