#https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ret = True
        def traverse(p,q,ret):
            if ret == False:
                return False
            if p == None or q == None:
                if p == None and q == None:
                    return True
                ret = False
                return False
            
            if p.val != q.val:
                ret = False
                return False
            
            
            return traverse(p.left,q.right,ret) and traverse(p.right,q.left,ret)
        
        return traverse(root,root,ret)