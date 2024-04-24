# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we can have two loops looking for two numbers but time will be O(n)^2
        dic = defaultdict(int) # value: index

        for i in range(len(nums)):
            diff = target - nums[i]
            if target - nums[i] in dic:
                return [i, dic[diff]]
            dic[nums[i]] = i
        return
        