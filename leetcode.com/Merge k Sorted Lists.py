"""
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k Sorted Lists
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        results = []

        for node in lists:
            curr = node
            while curr:
                results.append(curr.val)
                curr = curr.next
        results.sort()

        if results:
            root = ListNode(results.pop(0))
            curr = root
            for val in results:
                curr.next = ListNode(val)
                curr = curr.next

            return root
        else:
            return None
