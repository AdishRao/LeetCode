# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.traverse(root, low, high)
        return self.total

    def traverse(self, root, low, high):
        if (root.val >= low and root.val <= high):
            self.total += root.val
        if(root.left != None and root.val >= low):
            self.traverse(root.left, low, high)
        if(root.right != None and root.val <= high):
            self.traverse(root.right, low, high)