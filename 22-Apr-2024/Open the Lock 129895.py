# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = [0,0,0,0]
        ways = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0],
        [0,0,0,-1],[0,0,-1,0],[0,-1,0,0],[-1,0,0,0]]

        deadends = set(deadends)

        def toStr(num):
            return "".join(map(str,num))
        
        if toStr(start) in deadends:
            return -1
        
        queue = deque([(start,0)])
        deadends.add(toStr(start))

        while queue:
            num, d = queue.popleft()

            if toStr(num) == target:

                return d

            for way in ways:
                newNum = []
                for digit, inc in zip(num,way):
                    newNum.append((digit + inc) % 10)

                if toStr(newNum) not in deadends:
                    queue.append((newNum,d +1))
                    deadends.add(toStr(newNum))
        
        return -1

            


            
        