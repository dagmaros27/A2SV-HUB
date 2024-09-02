# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return [0,True]
            if root.left is None and root.right is None:
                return [1,True]
            
            left = [0,True]
            right = [0,True]            
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            
            balanced = abs(left[0] - right[0]) <= 1

            if not left[1] or not right[1]:
                balanced = False
            return 1 + max(left[0],right[0]), balanced

        ans = dfs(root)

        return ans[1]
            

        