#https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        def traverse(node, paths, cur_path=[]):
            if not node:
                return
            
            cur_path.append(str(node.val))
            if not node.left and not node.right:
                paths.append('->'.join(cur_path))
                cur_path.pop()
                return
            
            traverse(node.left,paths,cur_path)
            traverse(node.right,paths,cur_path)
            cur_path.pop()
            
            return
        
        traverse(root,paths)
        return paths
            