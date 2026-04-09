# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        vals = []
        cur_head = head
        while cur_head:
            vals.append(cur_head.val)
            cur_head = cur_head.next

        reordered_vals = []
        l, r = 0, (len(vals) - 1)
        while l <= r:
            if l == r:
                reordered_vals.append(vals[l])
                break
            reordered_vals.extend([vals[l], vals[r]])
            l += 1
            r -= 1

        cur_node = head
        idx = 0
        while cur_node:
            cur_node.val = reordered_vals[idx]
            idx += 1
            cur_node = cur_node.next