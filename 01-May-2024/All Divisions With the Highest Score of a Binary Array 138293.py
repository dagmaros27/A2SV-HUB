# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        highest = []
        highest_score = float("-inf")
        total_ones = nums.count(1)
        zeros = 0
        ones = 0
        for i in range(len(nums)+1):

            total = zeros + (total_ones - ones)
            if i < len(nums):
                if nums[i] == 1:
                    ones += 1
                elif nums[i] == 0:
                    zeros += 1
            if total > highest_score:
                highest_score = total
                highest = [i]
            elif total == highest_score:
                highest.append(i)


        # for i in range(len(nums)+1):
        #     zeros = nums[:i].count(0)
        #     ones = nums[i:].count(1)
        #     total = zeros + ones
        #     if total > highest_score:
        #         highest_score = total
        #         highest = [i]
        #     elif total == highest_score:
        #         highest.append(i)
        
        return highest



