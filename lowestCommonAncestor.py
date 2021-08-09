#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = root
        while(True):
            if(p.val<=node.val):
                if (q.val>=node.val or p.val==node.val):
                    return node
                else:
                    node = node.left
            else:
                if (q.val<=node.val):
                    return node
                else:
                    node = node.right