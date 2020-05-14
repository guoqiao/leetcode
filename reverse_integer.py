class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = x > 0
        n = abs(x)
        m = int(str(n)[::-1])
        if m > pow(2, 31):
            return 0
        return m if flag else 0 - m

if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(100) == 1
