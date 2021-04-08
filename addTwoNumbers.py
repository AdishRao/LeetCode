#https://leetcode.com/problems/add-two-numbers/submissions/
# Definiton for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        ret_val = res
        prev = None
        rem = 0
        while(l1!=None and l2!=None):
            res.val = l1.val + l2.val + rem
            rem = 0
            if(res.val>=10):
                rem = 1
                res.val -= 10
            res.next = ListNode()
            prev = res
            res = res.next
            l1 = l1.next
            l2 = l2.next
        if(l1!=None):
            while(l1!=None):
                res.val = l1.val + rem
                rem = 0
                if(res.val>=10):
                    rem = 1
                    res.val -= 10
                res.next = ListNode()
                prev = res
                res = res.next
                l1 = l1.next
            
        elif(l2!=None):
            while(l2!=None):
                res.val = l2.val + rem
                rem = 0
                if(res.val>=10):
                    rem = 1
                    res.val -= 10
                res.val = res.val
                res.next = ListNode()
                prev = res
                res = res.next
                l2 = l2.next
        if rem!=0:
            res.val = 1
            res.next = ListNode()
            prev = res
            res = res.next
        prev.next = None
        return ret_val