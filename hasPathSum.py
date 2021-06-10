#https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def check_path(node,sum_):
            if self.ret or node == None:
                return

            sum_ += node.val
            
            if node.left == None and node.right == None:
                if sum_ == targetSum:
                    self.ret = True
                return
            
            check_path(node.left,sum_)
            check_path(node.right,sum_)
            
            return
        
        if root == None:
            return False
        
        self.ret = False
        check_path(root,0)
        return self.ret