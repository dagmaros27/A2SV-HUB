# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []

        def dfs(root):
            nonlocal ans
            if root is None:
                return
            if root.left is None and root.right is None:
                ans.append(str(root.val))
                return
            ans.append(str(root.val))

            if root.left:
                ans.append("(")
                dfs(root.left)
                ans.append(")")
            if root.left is None and root.right:
                ans.append("()")
            
            if root.right:
                ans.append("(")
                dfs(root.right)
                ans.append(")")
            

            return 

        dfs(root)


        return "".join(ans)
            


        