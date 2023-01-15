# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        while head is not None:
            q.append(head)
            head = head.next
        s=True
        dummy = ListNode()
        while len(q) > 0:
            if s:
                dummy.next = q.popleft()
            else:
                dummy.next = q.pop()
            dummy = dummy.next
            s = not s
        dummy.next = None
