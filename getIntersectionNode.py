#https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Using Dictionary
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic = {}
        node = headA
        
        while(node!=None):
            dic[node] = True
            node = node.next
        
        node = headB
        while(node!=None):
            if node in dic:
                return node
            node = node.next

#Using Len of the linklists
class Solution:
    def getIntersectionNode(self, headA, headB):
        currA, currB = headA, headB
        
        while currA != currB:
            currB = headA if currB is None else currB.next
            currA = headB if currA is None else currA.next
            
        return currA