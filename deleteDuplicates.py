#https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        cur = head
        next_ = head.next
        while(next_!=None):
            if cur.val == next_.val:
                cur.next = next_.next
                next_ = next_.next
                continue
            cur = next_
            next_ = next_.next
        return head