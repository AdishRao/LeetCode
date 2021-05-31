#https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.min_depth = 10**5
        self.max_depth = 10**5
        def traverse(node, depth):
            if node == None:
                return self.max_depth
            if (depth+1) >= self.min_depth:
                return self.min_depth
            if node.left == None and node.right == None:
                if (depth+1) < self.min_depth:
                    self.min_depth = (depth+1)
                return depth+1
            
            return min(traverse(node.left,depth+1), traverse(node.right,depth+1))
                 
        return traverse(root, 0)