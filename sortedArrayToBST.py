#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        len_ = len(nums)-1
        def insert(l,h):
            if l>h:
                return None
            if l==h:
                return TreeNode(nums[l])
            
            m = (l+h)//2
            
            node = TreeNode(nums[m])
            
            node.left = insert(l,m-1)
            node.right = insert(m+1,h)
            
            return node
        
        return insert(0,len_)