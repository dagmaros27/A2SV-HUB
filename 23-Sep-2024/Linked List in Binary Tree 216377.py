# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        paths = []

   
        def dfs(root, path):
            if root is None:
                return
            if root.left is None and root.right is None:
                path.append(root.val)
                paths.append(path.copy())
                return
            path.append(root.val)
            
            if root.left:
                dfs(root.left, path.copy())  
            if root.right:
                dfs(root.right, path)  

        def is_subset(arr, linkedList):
            n = len(arr)
            
            for i in range(n):
                curr = linkedList
                j = i
                
                while curr and j < n and curr.val == arr[j]:
                    curr = curr.next
                    j += 1
                
                if curr is None:
                    return True
            
            return False  
        dfs(root, [])
        
        for path in paths:
            if is_subset(path, head):
                return True
        return False
