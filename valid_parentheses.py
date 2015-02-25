class Solution:
    # @return a boolean
    def isValid(self, s):
        d = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                if stack and stack[-1] == d[c]:
                    del stack[-1]
                else:
                    return False
        return not stack

if __name__ == '__main__':
    s = Solution()
    assert s.isValid('()[]{}') == True
    assert s.isValid('([]){}') == True
    assert s.isValid(')[]({}') == False
    assert s.isValid('') == True
    assert s.isValid('[]') == True
    assert s.isValid('(()') == False
    assert s.isValid('([])') == True
    print 'pass'

        
