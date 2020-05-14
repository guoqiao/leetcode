class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        def reverse(nums, left, right):
            center = (right - left) / 2.0
            i = 0
            while i < center:
                t = nums[left + i]
                nums[left + i] = nums[right - i]
                nums[right - i] = t
                i += 1
        N = len(nums)
        k = k % N
        if k > 0:
            reverse(nums, 0, N-1) 
            reverse(nums, 0, k-1) 
            reverse(nums, k, N-1) 

if __name__ == '__main__':
    s = Solution()
    nums = range(7)
    s.rotate(nums, -1)
    print nums
