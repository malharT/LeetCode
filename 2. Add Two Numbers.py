# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        carry = 0
        while l1 is not None and l2 is not None:
            addition = l1.val + l2.val + carry
            num = addition%10
            carry = addition//10
            node.next = ListNode(val=num)
            l1 = l1.next
            l2 = l2.next
            node = node.next
        nums = None
        if l1 is not None:
            nums = l1
        elif l2 is not None:
            nums = l2
        while nums is not None:
            addition = nums.val + carry
            num = addition%10
            carry = addition//10
            node.next = ListNode(val=num)
            nums = nums.next
            node = node.next
        if carry != 0:
            node.next = ListNode(val=carry)
        return head.next
