# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = deque()
        ans = head
        while head:
            q.append(head)
            if len(q) > n+1:
                q.popleft()
            head = head.next
        if len(q) == n:
            if n == 1:
                return None
            else:
                return q[1]
        if len(q) > 2:
            q[0].next = q[2]
        else:
            q[0].next=None
        return ans