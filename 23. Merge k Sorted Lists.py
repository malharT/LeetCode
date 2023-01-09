# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        new_list = ListNode()
        list_head = new_list
        while(list1 is not None and list2 is not None):
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next

        if list1 is not None:
            new_list.next = list1
        if list2 is not None:
            new_list.next = list2
        return list_head.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            new_list = self.merge(lists[0], lists[1])
            return new_list
        else:
            l = len(lists)
            new_list1 = self.mergeKLists(lists[:l//2])
            new_list2 = self.mergeKLists(lists[l//2:])
            new_list = self.mergeKLists([new_list1, new_list2])
            return new_list
