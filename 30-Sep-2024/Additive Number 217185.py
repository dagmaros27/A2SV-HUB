# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def helper(a,b):
            p = [a,b]
            total = sum(len(x) for x in p)

            while total < n:
                next_num = str(int(p[-1]) + int(p[-2]))
                p.append(next_num)
                total += len(next_num)

            return "".join(p)

        for l in range(1,n):
            for r in range(l+1, n):
                num1 = num[:l]
                num2 = num[l:r]
                if num[l] == "0" and r-l > 1:
                    break
                s = helper(num1,num2)

                if s == num:
                    return True
                
            if num[0] == "0":
                break

        return False
        