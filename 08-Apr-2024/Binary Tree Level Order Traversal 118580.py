# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        order = []
        queue = deque()
        queue.append(root)

        if not root:
            return []
        def bfs(queue,order):

            values = []
            while queue :
                lvl = len(queue)

                while lvl > 0:

                    node = queue.popleft()
                    values.append(node.val)
                    

                    node.left and queue.append(node.left)
                    node.right and queue.append(node.right)

                    lvl -= 1
                    
                order.append(values.copy())
                values.clear()
        
        bfs(queue,order)

        return order
        