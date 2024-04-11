# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents, queue, visited = {}, collections.deque([(target, 0)]), set()
        self.getParents(root, None, parents)
        
        res = []
        while queue:
            node, dist = queue.popleft()   
            if node not in visited:
                if dist == k: res.append(node.val)
                visited.add(node)
                
                if node.left: queue.append((node.left, dist+1))
                if node.right: queue.append((node.right, dist+1))
                if parents[node]: queue.append((parents[node], dist+1))
        
        return res
        
    def getParents(self, root, parent, hmap):
        if not root:
            return 
        hmap[root] = parent
        if root.left: self.getParents(root.left, root, hmap)
        if root.right: self.getParents(root.right, root, hmap)