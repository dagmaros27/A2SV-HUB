# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 0)]
        max_width = 0
        while queue:
            level_size = len(queue)
            left_pos = queue[0][1]
            right_pos = queue[-1][1]
            max_width = max(max_width, right_pos - left_pos + 1)
            for i in range(level_size):
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2 + 1))
            for i in range(len(queue)):
                queue[i] = (queue[i][0], queue[i][1] - left_pos)
        return max_width