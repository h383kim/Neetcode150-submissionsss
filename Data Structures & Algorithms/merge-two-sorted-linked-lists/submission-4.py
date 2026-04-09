# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_new = ListNode(val=0)
        new_head = cur_new
        while list1 or list2:
            if list1 is None:
                cur_new.next = list2
                break
            elif list2 is None:
                cur_new.next = list1
                break
            else:
                if list1.val <= list2.val:
                    cur_new.next = list1
                    cur_new = cur_new.next
                    list1 = list1.next
                else:
                    cur_new.next = list2
                    cur_new = cur_new.next
                    list2 = list2.next
        new_head = new_head.next
        return new_head