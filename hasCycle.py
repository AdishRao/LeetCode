#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        next = head
        
        while(cur!=None and next!=None):
            cur = cur.next
            next = next.next
            if next!=None:
                next = next.next
            
            if cur == next and cur!=None:
                return True
        
        return False