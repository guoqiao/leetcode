# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        lst = []
        n = self
        while n:
            lst.append(n.val)
            n = n.next
        return lst


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        root = n3 = ListNode(0)
        flag = 0
        while n1 or n2 or flag:
            x = flag
            if n1:
                x += n1.val
                n1 = n1.next
            if n2:
                x += n2.val
                n2 = n2.next
            flag, x = divmod(x, 10)
            n3.next = ListNode(x)
            n3 = n3.next
        return root.next



if __name__ == '__main__':
    s = Solution()
