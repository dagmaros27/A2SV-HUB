# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr,idx):
            if idx == len(nums):
                ans.append(curr.copy())
            
            else:
                curr_val = nums[idx]

                curr.append(curr_val)
                backtrack(curr, idx+1)
                
                curr.pop()
                backtrack(curr, idx+1)
        
        ans = []
        backtrack([], 0)
        return ans

        
            
        