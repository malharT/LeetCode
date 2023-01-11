# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        v = ListNode(0,None)
        while head is not None:
            if head.next == v:
                return True
            temp = head.next
            head.next = v
            head = temp
        return False
