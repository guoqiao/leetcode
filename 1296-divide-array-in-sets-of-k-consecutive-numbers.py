#!/usr/bin/env python3

from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        count = Counter(nums)
        for num in sorted(count.keys()):
            if count[num] > 0:
                base = count[num]
                for n in range(num, num+k):
                    if count[n] < base:
                        return False
                    count[n] -= base
        return True


    def isPossibleDivide0(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        if len(nums) == k:
            return nums == list(range(nums[0], nums[0]+k))
        else:
            start = nums[0]
            for n in range(start, start+k):
                try:
                    nums.remove(n)
                except ValueError:
                    return False
            return self.isPossibleDivide(nums, k)


s = Solution()
assert s.isPossibleDivide([1], 1) is True
assert s.isPossibleDivide([1,2], 1) is True
assert s.isPossibleDivide([1,2], 2) is True
assert s.isPossibleDivide([1,2,3,4], 3) is False
assert s.isPossibleDivide([3,3,2,2,1,1], 3) is True
assert s.isPossibleDivide([1,2,3,3,4,4,5,6], 4) is True
assert s.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3) is True