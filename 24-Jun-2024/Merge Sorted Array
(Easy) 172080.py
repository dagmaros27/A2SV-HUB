# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        l1,r1 = m-1, len(nums1)-1
        r2 = n-1

        while r2>=0 and l1>=0:
            if nums1[l1] <= nums2[r2]:
                nums1[r1] = nums2[r2]
                r2 -= 1
            else:
                nums1[r1] = nums1[l1]
                l1 -= 1
            r1 -= 1

            
        while r2 >= 0:
            nums1[r1] = nums2[r2]
            r1 -= 1
            r2 -= 1

        
        