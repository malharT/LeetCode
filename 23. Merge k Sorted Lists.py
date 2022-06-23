class Solution:
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        list1_node = list1
        list2_node = list2
        if list1_node.val < list2_node.val:
            list1 = list1_node.next
            list1_node.next = None
            new_list_head = list1_node

        else:
            list2 = list2_node.next
            list2_node.next = None
            new_list_head = list2_node
        new_list = new_list_head

        while(list1 is not None and list2 is not None):
            list1_node = list1
            list2_node = list2
            if list1_node.val < list2_node.val:
                list1 = list1_node.next
                list1_node.next = None
                new_list.next = list1_node

            else:
                list2 = list2_node.next
                list2_node.next = None
                new_list.next = list2_node
            new_list = new_list.next

        if list1 is None and list2 is not None:
            new_list.next = list2
        if list1 is not None and list2 is None:
            new_list.next = list1
        return new_list_head

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
