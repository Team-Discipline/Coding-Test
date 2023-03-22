"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
Design Add and Search Words Data Structure
"""
from unittest import TestCase


class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        self.d[word] = True

    def search(self, word: str) -> bool:
        ready = list(filter(lambda x: len(x) == len(word), self.d.keys()))
        if not ready:
            return False

        valid_chars = []
        for i, ch in enumerate(word):
            if ch != '.':
                valid_chars.append(i)

        if len(valid_chars) != len(word):
            for can_index, candidate in enumerate(ready):
                for i, ch in enumerate(candidate):
                    if i not in valid_chars:
                        ready[can_index] = ready[can_index][:i] + '.' + ready[can_index][i + 1:]

        if word in ready:
            return True
        else:
            return False


class Case(TestCase):

    # def test1(self):
    #     commands = ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord",
    #                 "search", "search", "search", "search", "search", "search"]
    #     inputs = [[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."],
    #               ["a.d"], ["."]]
    #
    #     actual = self.run_with(commands, inputs)
    #     expected = [None, None, None, None, None, False, False, None, True, True, False, False, True, False]
    #     self.assertEqual(actual, expected)

    def test2(self):
        commands = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
        inputs = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
        actual = self.run_with(commands, inputs)
        expected = [None, None, None, None, False, True, True, True]
        self.assertEqual(actual, expected)

    def run_with(self, commands: [str], inputs: [str]) -> [None | bool]:
        res = []
        s = WordDictionary()
        for command, input_value in list(zip(commands, inputs)):
            if command == 'WordDictionary':
                res.append(None)
            elif command == 'addWord':
                s.addWord(input_value[0])
                res.append(None)
            elif command == 'search':
                res.append(s.search(input_value[0]))
        return res
