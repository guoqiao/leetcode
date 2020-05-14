#!/usr/bin/env python3

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num/2)
        else:
            return 1 + self.numberOfSteps(num-1)








s = Solution()
def test(num, expected_steps):
    assert s.numberOfSteps(num) == expected_steps


test(0, 0)
test(1, 1)
test(2, 2)
test(14, 6)
test(8, 4)
test(123, 12)