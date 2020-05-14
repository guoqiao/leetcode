class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num < 1:
            return ''
        K = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if num <= 26:
            return K[num]
        d, num = divmod(num, 26)
        if num == 0:
            d -= 1
            num = 26
        return self.convertToTitle(d) + K[num]

if __name__ == '__main__':
    s = Solution()
    K = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for num in range(1, 27):
        assert s.convertToTitle(num) == K[num]

    assert s.convertToTitle(1) == 'A'
    assert s.convertToTitle(26) == 'Z'
    assert s.convertToTitle(27) == 'AA'
    assert s.convertToTitle(28) == 'AB'
    assert s.convertToTitle(29) == 'AC'
    assert s.convertToTitle(52) == 'AZ'
    assert s.convertToTitle(53) == 'BA'
    assert s.convertToTitle(78) == 'BZ'
