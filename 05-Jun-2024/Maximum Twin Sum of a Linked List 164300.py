# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sums = []
        while head:
            sums.append(head.val)
            head = head.next
        
        l,r,mxm = 0,len(sums)-1, 0
        while l < r:
            pairSum = sums[l] + sums[r]
            mxm = max(mxm, pairSum)
            l += 1
            r -= 1
        return mxm


        