# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1==None and l2==None):
            return None
        
        root = ListNode()
        temp = root
        prev = temp
        
        while(l1!=None and l2!=None):
            if(l1.val<=l2.val):
                temp.val = l1.val
                temp.next = ListNode()
                prev = temp
                temp = temp.next
                l1 = l1.next
            if(l1!=None and l2.val<=l1.val):
                temp.val = l2.val
                temp.next = ListNode()
                prev = temp
                temp = temp.next
                l2 = l2.next
        
        while(l1!=None):
            temp.val = l1.val
            temp.next = ListNode()
            prev = temp
            temp = temp.next
            l1 = l1.next
            
        while(l2!=None):
            temp.val = l2.val
            temp.next = ListNode()
            prev = temp
            temp = temp.next
            l2 = l2.next
            
        prev.next = None
        return root