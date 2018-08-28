#!/usr/bin/env python

class Solution(object):
    def romanToInt(self, s):
        """
        :type x: str
        :rtype: int
        """
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        values = []
        for symbol in s.upper():
            value = symbols[symbol]
            if values and values[-1] < value:
                values[-1] = -values[-1]
            values.append(value)
        return sum(values)


if __name__ == '__main__':
    items = [
        ('I', 1),
        ('II', 2),
        ('III', 3),
        ('IV', 4),
        ('V', 5),
        ('VI', 6),
        ('VII', 7),
        ('VIII', 8),
        ('IX', 9),
        ('X', 10),
        ('XI', 11),
        ('XII', 12),
        ('XXVII', 27),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        ('DCXXI', 621),
    ]

    s = Solution()
    for k, v in items:
        assert(s.romanToInt(k) == v)

