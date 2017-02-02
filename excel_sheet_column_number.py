class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        K = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        V = range(1, 27)
        D = {k: v for k, v in zip(K, V)}
        r = 0
        for c in s:
            r = 26 * r + D[c] 
        return r

if __name__ == '__main__':
    s = Solution()
    K = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    V = range(1, 27)
    D = {k: v for k, v in zip(K, V)}
    for k in K:
        assert s.titleToNumber(k) == D[k]

    assert s.titleToNumber('AA') == 27
    assert s.titleToNumber('AB') == 28
        
