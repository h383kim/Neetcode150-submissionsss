# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        reverse_head = None
        for i in range(len(stack)):
            if i == 0:
                reverse_head = ListNode(val = stack.pop())
                cur = reverse_head
            else: 
                cur.next = ListNode(val = stack.pop())
                cur = cur.next
        
        return reverse_head