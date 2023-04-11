"""
https://leetcode.com/problems/palindrome-linked-list/description/
Palindrome Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        v = []
        curr = head
        while curr:
            v.append(curr.val)
            curr = curr.next
        if v == v[::-1]:
            return True
        else:
            return False
