#!/usr/bin/env python3

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        from collections import Counter
        v = Counter(arr).values()
        return len(v) == len(set(v))
        

s = Solution()
def test(arr, expected):
    assert s.uniqueOccurrences(arr) == expected

test([1,2,2,1,1,3], True)
test([1], True)
test([1,2], False)
test([-3,0,1,-3,1,1,1,-3,10,0], True)