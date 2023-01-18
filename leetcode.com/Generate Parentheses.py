"""
https://leetcode.com/problems/generate-parentheses/
Generate Parentheses
"""


class Solution:
    def make(self, n: int, stack: str, results: [str]):
        height_limit = n * 2
        if 0 < len(stack) < height_limit:
            # Stack is not full yet!
            # We can insert "()" in every single index!
            for index in range(len(stack)):
                self.make(n, stack[:index + 1] + '()' + stack[index + 1:], results)
        elif len(stack) == 0 and n > 0:
            self.make(n, '()', results)
        elif len(stack) == height_limit and n > 0:
            results.append(stack)

    def generateParenthesis(self, n: int) -> [str]:
        results = []

        self.make(n, '', results)

        results = list(set(results))
        return results


s = Solution()
assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
assert s.generateParenthesis(1) == ["()"]
