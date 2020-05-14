#!/usr/bin/env python3

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # return sum(s in J for s in S)
        # return sum(map(J.count, S))
        return sum(map(S.count, J))



s = Solution()
def test(J, S, expected):
    assert s.numJewelsInStones(J, S) == expected


test('aA', 'aAAbbb', 3)
test('z', 'ZZ', 0)
test('ab', 'aaabbbccc', 6)