# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        traversed = []
        def dfs(root):
            nonlocal traversed
            if root is None:
                return 
            
            for child in root.children:
                dfs(child)

            traversed.append(root.val)
            return
        
        dfs(root)

        return traversed

        