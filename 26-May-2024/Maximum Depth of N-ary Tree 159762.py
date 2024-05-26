# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if root is None:
                return 0
            mxm = 0
            
            for node in root.children:
                mxm = max(mxm, dfs(node))     
            
            return 1 + mxm
        return dfs(root)
        