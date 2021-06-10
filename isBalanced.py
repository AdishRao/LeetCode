#https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ret = True
        def traverse(node, depth):
            if not self.ret:
                return 0
            if node == None:
                return depth
            
            l = traverse(node.left,depth+1)
            r = traverse(node.right,depth+1)
            
            if (abs(l-r)>1):
                self.ret = False
            
            return max(l,r)
            
            
                 
        traverse(root, 0)
        return self.ret