# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(path,root):
            if not root:
                return
            if not root.left and not root.right:
                path.append(root.val)
                paths.append(path)
                return
            path.append(root.val)
            dfs(path.copy(),root.left)
            dfs(path,root.right)
            return
        dfs([],root)

        ans = []

        for p in paths:
            ans.append("->".join(map(str,p)))
        
        return ans
            
        