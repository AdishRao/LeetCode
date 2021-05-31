# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ret = True

        def traverse(p, q, ret):
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

            return traverse(p.left, q.left, ret) and traverse(p.right, q.right, ret)

        return traverse(p, q, ret)
