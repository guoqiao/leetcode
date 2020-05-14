#!/usr/bin/env python3

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        N = max(*candies)
        return [n+extraCandies>=N for n in candies]



def test(candies, extraCandies, expected_results):
    s = Solution()
    assert s.kidsWithCandies(candies, extraCandies) == expected_results


test([2,3,5,1,3], 3, [True, True, True, False, True])
test([4,2,1,1,2], 1, [True,False,False,False,False])
test([12,1,12], 10, [True, False, True])
test([1,1,1], 1, [True, True, True])