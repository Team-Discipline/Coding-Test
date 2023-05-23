"""
https://leetcode.com/problems/generate-parentheses/
Generate Parentheses
"""
from functools import lru_cache
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        @lru_cache(maxsize=None)
        def find_char_indices(ch: str, s: str) -> List[int]:
            res = []
            for i, c in enumerate(s):
                if ch == c:
                    res.append(i)
            return res

        @lru_cache(maxsize=None)
        def make(given: str, count: int):
            nonlocal n, res
            if count == n:
                res.append(given)
                return
            for i in find_char_indices(')', given):
                make(given[:i] + '()' + given[i:], count + 1)
                make(given[:i + 1] + '()' + given[i + 1:], count + 1)

        make('()', 1)
        return sorted(list(set(res)))


s = Solution()
assert s.generateParenthesis(3) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
assert s.generateParenthesis(1) == sorted(["()"])
