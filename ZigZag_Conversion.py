class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows < 2:
            return s
        N = len(s)
        if N < 2:
            return s
        U = nRows + nRows - 2
        x, y = divmod(N, U)
        if y > 0:
            x += 1
            for i in range(U - y):
                s += ' '
        A = []
        for i in range(x):
            a1 = [s[i * U + j] for j in range(nRows)]
            a2 = [' ' for j in range(nRows)]
            for j in range(nRows-2):
                a2[-2-j] = s[i * U + nRows + j]
            A.append(a1)
            A.append(a2)
        out = ''
        for i in range(nRows):
            for a in A:
                c = a[i].strip()
                if c:
                    out += a[i]
        return out


if __name__ == '__main__':
    s = Solution()
    print s.convert('PAYPALISHIRING', 3)
    print s.convert('A', 1)
    print s.convert('AB', 2)
