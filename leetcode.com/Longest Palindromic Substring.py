"""
https://leetcode.com/problems/longest-palindromic-substring/
Longest Palindromic Substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r + 1]
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r + 1]
                l -= 1
                r += 1
        return result


s = Solution()
assert s.longestPalindrome("abb") == 'bb'
assert s.longestPalindrome("cbbd") == 'bb'
assert s.longestPalindrome('aacabdkacaa') == 'aca'
assert s.longestPalindrome("a") == "a"
assert s.longestPalindrome('ac') == 'a'
assert s.longestPalindrome("bb") == 'bb'
assert s.longestPalindrome("babad") == 'bab'
