#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        prev = None
        next = cur.next
        while(cur):
            prev = cur
            cur = next
            if cur:
                next = cur.next
                cur.next = prev
            
        head.next = None
        head = prev
        return head