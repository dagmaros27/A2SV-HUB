# Problem: Three sum - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       ans = set()
        nums.sort()
        
        for  i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            j , k = i+1,len(nums)-1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -=1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1    
        return list(ans)