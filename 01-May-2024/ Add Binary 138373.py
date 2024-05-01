# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # length = min(len(a), len(b))

        # ans = []
        # carry = 0
        # for i in range(length-1,-1,-1):
        #     if carry:
        #         if (a[i] == "1" and b[i] == "1") or (a[i] == "0" and b[i] == "0"):
        #             ans.append("1")
        #             if a[i] == "0":
        #                 carry = 0
        #         else:
        #             ans.append("1")
        #     else:
        #         if (a[i] == "1" and b[i] == "1"):
        #             ans.append("0")
        #             carry = 1
        #         elif (a[i] == "0" and b[i] == "0"):
        #             ans.append("0")
        #         else:
        #             ans.append("1")
            
        # if len(a) > len(b):
        #     j = len(a) - length-1
        #     while j >=0 and carry:
        #         if a[j] == "1":
        #             ans.append("0")
        #         else:
        #             ans.append("1")
        #             carry = 0
        #         j -= 1
        #     if a[:j]: ans.append(a[:j]) 
        # elif len(a) < len(b):
        #     j = len(b) - length-1
        #     while j >=0 and carry:
        #         if b[j] == "1":
        #             ans.append("0")
        #         else:
        #             ans.append("1")
        #             carry = 0
        #         j -= 1
        #     if b[:j]: ans.append(b[:j]) 

        # if carry:
        #     ans.append("1")
                
        # print(ans)
        a = int(a,2)
        b = int(b,2)

        a+= b
        return bin(a)[2:]
                


        