#https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        def traverse(node, new_root):
            if node.right:
                new_root.left = TreeNode(node.right.val)
                traverse(node.right, new_root.left)
            else:
                new_root.left = None
            if node.left:
                new_root.right = TreeNode(node.left.val)
                traverse(node.left, new_root.right)
            else:
                new_root.right = None
            
            
        new_root = TreeNode(root.val)
        traverse(root, new_root)
        
        return new_root