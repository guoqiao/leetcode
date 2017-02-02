class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = [int(d) for d in version1.split('.')]
        v2 = [int(d) for d in version2.split('.')]
        n1 = len(v1)
        n2 = len(v2)
        n = n1
        if n1 > n2:
            n = n1
            diff = n1 - n2
            for i in range(diff):
                v2.append(0)
        elif n1 < n2:
            n = n2
            diff = n2 - n1
            for i in range(diff):
                v1.append(0)
        i = 0
        while i < n:
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        return 0

if __name__ == '__main__':
    s = Solution()
    assert s.compareVersion('0.1', '1.1') == -1
    assert s.compareVersion('2.1', '2.0') == 1
    assert s.compareVersion('2.1', '2.1') == 0
    assert s.compareVersion('2.1.0', '2.1') == 0
    assert s.compareVersion('2.1.1', '2.1') == 1
    assert s.compareVersion('2.1', '13.37') == -1
