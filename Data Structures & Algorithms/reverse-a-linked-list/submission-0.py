# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        left = None
        while current is not None:
            hold = current.next
            current.next = left
            left = current
            current = hold
        return left

            


