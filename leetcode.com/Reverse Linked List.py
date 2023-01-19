"""
https://leetcode.com/problems/reverse-linked-list/
Reverse Linked List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        stack = []
        result = None

        while head is not None:
            stack.append(head.val)  # 1, 2, 3, 4, 5
            head = head.next

        while stack:
            temp = ListNode(val=stack.pop())  # 5, 4, 3, 2, 1
            if result is None:
                result = temp
            else:
                t = result
                while t.next is not None:
                    t = t.next
                t.next = temp

        return result


s = Solution()
assert s.reverseList(
    ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))) \
       == ListNode(val=5,
                   next=ListNode(val=4, next=ListNode(val=3, next=ListNode(val=2, next=ListNode(val=1, next=None)))))
