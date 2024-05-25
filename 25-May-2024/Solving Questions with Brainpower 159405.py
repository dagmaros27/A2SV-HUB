# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        mxm = [0]*n
        dp[n-1] = questions[n-1][0]
        mxm[n-1] = dp[n-1]

        for i in range(n-2,-1,-1):
            if i + questions[i][1]+1 < n:
                dp[i] = questions[i][0] + max(mxm[i +  questions[i][1]+1], dp[i + questions[i][1]+1])
            else:
                dp[i] = questions[i][0]
            mxm[i] = max(dp[i], mxm[i+1])

        return max(dp)


        