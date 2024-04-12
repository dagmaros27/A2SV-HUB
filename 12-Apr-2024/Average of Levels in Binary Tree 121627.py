# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        lvls = []

        queue = deque([root])

        while queue:
            t = len(queue)
            acc = []
            div= t
            while t:
                n = queue.popleft()
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                acc.append(n.val)
                t -=1 
            avg = sum(acc)/div
            lvls.append(avg)
            acc.clear()
        

        return lvls
                
                
        