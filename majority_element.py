class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        D = {}
        N = len(num)/2
        for n in num:
            c = D.get(n, 0) + 1
            if c > N:
                return n
            D[n] = c

if __name__ == '__main__':
    s = Solution()
    assert s.majorityElement([2,2,3]) == 2
    assert s.majorityElement([6,5,5]) == 5
    assert s.majorityElement([2,2,2,3,4,5,2]) == 2

