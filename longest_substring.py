class Solution(object):
    def lengthOfLongestSubstring0(self, s):
        """
        :type str: str
        :rtype: int
        """
        N = len(s)
        tmp_max = 0
        for i in range(0, N):
            if N - i <= tmp_max:
                break
            memo = set()
            for j in range(i, N):
                if s[j] not in memo:
                    memo.add(s[j])
                else:
                    if len(memo) > tmp_max:
                        tmp_max = len(memo)
                    break
        return tmp_max

    def lengthOfLongestSubstring1(self, s):
        """
        :type str: str
        :rtype: int
        """
        if not s:
            return 0

        N = len(s)
        for offset in range(N):
            M = N - offset
            for start in range(0, offset+1):
                x = s[start:start+M]
                if len(set(x)) == M:
                    print(M)
                    return M

    def lengthOfLongestSubstring(self, s):
        """
        :type str: str
        :rtype: int
        """
        if not s:
            return 0

        d = {}
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(d[c], start)
            else:
                max_len = max(i-start, max_len)
            d[c] = i
            print(i, c, start, max_len)
        return max_len


if __name__ == '__main__':
    s = Solution()
    # assert s.lengthOfLongestSubstring(None) == 0
    # assert s.lengthOfLongestSubstring('') == 0
    # assert s.lengthOfLongestSubstring('b') == 1  #'b'
    # assert s.lengthOfLongestSubstring('bb') == 1  #'b'
    # assert s.lengthOfLongestSubstring('bbb') == 1  #'b'
    # assert s.lengthOfLongestSubstring('bbbb') == 1  #'b'
    # assert s.lengthOfLongestSubstring('bbbbb') == 1  #'b'
    # assert s.lengthOfLongestSubstring('abcabcbb') == 3  #'abc'
    # assert s.lengthOfLongestSubstring('pwwkew') == 3  #'wke'
    # assert s.lengthOfLongestSubstring('abcabcbb') == 3  #'abc'
    # assert s.lengthOfLongestSubstring('abcdefg') == 7
    # assert s.lengthOfLongestSubstring('aab') == 2
    # assert s.lengthOfLongestSubstring('gabcdefg') == 7
    # assert s.lengthOfLongestSubstring('dvdf') == 3
    assert s.lengthOfLongestSubstring('tmmzuxt') == 5
    # assert s.lengthOfLongestSubstring("szevlbnejxdlryofhsivutxfgnojjgedgiatjpxunbgebwmjrwgnsdsathjepnivwkqhaocprktuihdzgm") == 17
