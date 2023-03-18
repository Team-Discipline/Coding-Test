"""
https://leetcode.com/problems/longest-palindromic-substring/
Longest Palindromic Substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxval = ''
        for i in range(len(s)):
            if len(maxval) > i * 2:
                continue

            # odd case
            append = len(maxval) // 2
            while -1 < i - append and i + append < len(s):
                block = s[i - append: i] + s[i] + s[i + 1: i + append + 1]
                if block == block[::-1]:
                    maxval = block
                append += 1

            # even case
            append = len(maxval) // 2
            while -1 < i - append and i + append + 1 < len(s):
                block = s[i - append: i + 2] + s[i + 2: i + append + 2]
                if block == block[::-1]:
                    maxval = block
                append += 1
        return maxval


s = Solution()
assert s.longestPalindrome("abb") == 'bb'
assert s.longestPalindrome("cbbd") == 'bb'
assert s.longestPalindrome('aacabdkacaa') == 'aca'
assert s.longestPalindrome("a") == "a"
assert s.longestPalindrome('ac') == 'a'
assert s.longestPalindrome("bb") == 'bb'
assert s.longestPalindrome("babad") == 'bab'
