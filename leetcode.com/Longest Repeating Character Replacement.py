"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
Longest Repeating Character Replacement
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxlen = 0

        left = 0
        maxf = 0
        for right in range(len(s)):
            d[s[right]] += 1
            maxf = max(maxf, d[s[right]])

            if (right - left + 1) - maxf > k:
                d[s[left]] -= 1
                left += 1

            maxlen = max(maxlen, right - left + 1)
        return maxlen


s = Solution()
assert s.characterReplacement("BAAAB", 2) == 5
assert s.characterReplacement("ABBB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
