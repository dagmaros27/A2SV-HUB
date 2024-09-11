# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mxm = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            prev_mxm = mxm
            mxm = max(mxm, arr[i])
            arr[i] = prev_mxm
        
        return arr
        