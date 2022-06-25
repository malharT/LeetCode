# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, list_to_reverse):
        prev_node = None
        tail = list_to_reverse
        while(list_to_reverse is not None):
            temp = list_to_reverse.next
            list_to_reverse.next = prev_node
            prev_node = list_to_reverse
            list_to_reverse = temp
        return prev_node, tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heads_to_reverse = []
        cur_head = head
        head_not_to_reverse = None
        while cur_head is not None:
            i = 1
            while i < k:
                head = head.next
                if head is not None:
                    i += 1
                else:
                    break
            if i == k:
                heads_to_reverse.append(cur_head)
                cur_head = head.next
                head.next = None
                head = cur_head
            else:
                head_not_to_reverse = cur_head
                cur_head = head
        lists_to_append = []
        for head in heads_to_reverse:
            lists_to_append.append(self.reverse_list(head))
        if head_not_to_reverse is not None:
            lists_to_append.append((head_not_to_reverse, None))
        final_head, old_tail = lists_to_append.pop(0)
        for head, tail in lists_to_append:
            old_tail.next = head
            old_tail = tail
        return final_head
