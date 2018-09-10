#!/usr/bin/env python

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ['']
        for x in zip(*strs):
            if x.count(x[0]) == len(x):
                r.append(x[0])
            else:
                break
        return ''.join(r)



if __name__ == '__main__':
    fixtures = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["dog", "dog", "dog"], "dog"),
        (["dog", "dogcat", "doggy"], "dog"),
        (["dog"], "dog"),
        ([""], ""),
    ]
    s = Solution()
    for item in fixtures:
        assert s.longestCommonPrefix(item[0]) == item[1]
