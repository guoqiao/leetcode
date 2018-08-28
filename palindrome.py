#!/usr/bin/env python

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        stack = []
        while x > 0:
            x, y = divmod(x, 10)
            stack.append(y)
        return list(reversed(stack)) == stack


if __name__ == '__main__':
    s = Solution()

    # import pdb; pdb.set_trace()
    assert(s.isPalindrome(0))
    assert(s.isPalindrome(1))
    assert(s.isPalindrome(9))
    assert(s.isPalindrome(121))
    assert(s.isPalindrome(1234567654321))
    assert(s.isPalindrome(1221))

    assert(not s.isPalindrome(10))
    assert(not s.isPalindrome(100))
    assert(not s.isPalindrome(123))
    assert(not s.isPalindrome(-121))
