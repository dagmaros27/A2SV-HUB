# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        pairs = []

        for i in range(len(nums)):
            val = 0
            temp = nums[i]

            place = 1
            if temp == 0:
                pairs.append((mapping[0], i))
                continue
            while temp != 0:
                val = place * mapping[temp % 10] + val
                place *= 10
                temp //= 10
            pairs.append((val, i))

        pairs.sort()
        for pair in pairs:
            res.append(nums[pair[1]])    

        return res