"""
https://leetcode.com/problems/minimum-window-substring/
Minimum Window Substring
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        for ch in t:
            if ch not in s:
                return ''

        minval = str(s)

        # dt = {}
        # for ch in t:
        #     dt[ch] = 1 + dt.get(ch, 0)

        have, need = 0, len(t)
        left = 0
        for right, ch in enumerate(s):
            have += 1
            block = s[left: right + 1]
            if s[right] in t:
                need -= 1

            if need == 0:
                if len(minval) > (right - left + 1):
                    minval = s[left: right + 1]
                    left += 1
                    have -= 1
                    need += 1

            while s[left] not in t and left <= right:
                block = s[left: right + 1]
                have -= 1
                left += 1

        return minval


s = Solution()
# actual = s.minWindow('ab', 'b')
# print(f'{actual=}')
# assert actual == 'b'

actual = s.minWindow("ADOBECODEBANC", "ABC")
print(f'{actual=}')
assert actual == 'BANC'
