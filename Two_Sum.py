class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        for i in range(0, N-1):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()
    nums = range(10)
    assert s.twoSum(nums, 1) == [0, 1]
    assert s.twoSum(nums, 2) == [0, 2]
    nums = [2, 7, 11, 15]
    assert s.twoSum(nums, 9) == [0, 1]
    assert s.twoSum(nums, 26) == [2, 3]
