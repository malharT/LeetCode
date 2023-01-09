# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_head = head
        stack = []
        ans = ListNode()
        ans.next = head
        last_tail = ans
        while cur_head is not None:
            stack.append(cur_head)
            cur_head = cur_head.next
            if len(stack) == k:
                node = stack.pop()
                last_tail.next = node
                while len(stack) > 0:
                    temp =  stack.pop()
                    node.next = temp
                    node = node.next
                last_tail = node
        if len(stack) > 0:
            last_tail.next = stack[0]
        else:
            last_tail.next = None
        return ans.next
