# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x,y = nums[:n], nums[n:]

        i = 0
        j = 1
        while i < len(y):
            x.insert(i+j, y[i])
            i += 1
            j += 1

        return x 