# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(idx, arr):
            if idx == len(s):
                ans.append("".join(arr.copy()))
                return
            if s[idx].isnumeric():
                arr.append(s[idx])
                backtrack(idx+1, arr)
                arr.pop()

            else:
                letter = s[idx].swapcase()
                arr.append(letter)
                backtrack(idx+1, arr)
                arr.pop()
                arr.append(s[idx])
                backtrack(idx+1, arr)
                arr.pop()
            return
        backtrack(0,[])

        return ans
        