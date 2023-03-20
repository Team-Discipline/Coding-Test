"""
https://leetcode.com/problems/minimum-window-substring/
Minimum Window Substring
"""
from unittest import TestCase


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Struggled with this problem for a long while.
        # Idea: Two pointers: moving end forward to find a valid window,
        #                     moving start forward to find a smaller window
        #                     counter and hash_map to determine if the window is valid or not

        # Count the frequencies for chars in t
        hash_map = dict()
        for ch in t:
            hash_map[ch] = 1 + hash_map.get(ch, 0)

        start, end = 0, 0

        # If the minimal length doesn't change, it means there's no valid window
        min_window_length = len(s) + 1  # To check initial window is changed.

        # Start point of the minimal window
        min_window_start = 0

        # Works as a counter of how many chars still need to be included in a window
        num_of_chars_to_be_included = len(t)

        while end < len(s):
            # If the current char is desired
            if s[end] in hash_map:
                # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
                if hash_map[s[end]] > 0:
                    num_of_chars_to_be_included -= 1
                # And we decrease the hash_map value
                hash_map[s[end]] -= 1

            # If the current window has all the desired chars
            while num_of_chars_to_be_included == 0:
                # See if this window is smaller
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window_start = start

                # if s[start] is desired, we need to update the hash_map value and the counter
                if s[start] in hash_map:
                    hash_map[s[start]] += 1
                    # Still, update the counter only if the current char is "critical"
                    if hash_map[s[start]] > 0:
                        num_of_chars_to_be_included += 1

                # Move start forward to find a smaller window
                start += 1

            # Move end forward to find another valid window
            end += 1

        if min_window_length == len(s) + 1:
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]


class Case(TestCase):
    s = Solution()

    def test1(self):
        actual = self.s.minWindow("ADOBECODEBANC", "ABC")
        expected = 'BANC'
        self.assertEqual(actual, expected)

    def test2(self):
        actual = self.s.minWindow('ab', 'b')
        expected = 'b'
        self.assertEqual(actual, expected)

    def test3(self):
        actual = self.s.minWindow('a', 'aa')
        exected = ''
        self.assertEqual(actual, exected)

    def test4(self):
        actual = self.s.minWindow('a', 'a')
        expected = 'a'
        self.assertEqual(actual, expected)

    def test5(self):
        actual = self.s.minWindow('a', 'b')
        expected = ''
        self.assertEqual(actual, expected)

    def test6(self):
        actual = self.s.minWindow('bba', 'ba')
        expected = 'ba'
        self.assertEqual(actual, expected)
