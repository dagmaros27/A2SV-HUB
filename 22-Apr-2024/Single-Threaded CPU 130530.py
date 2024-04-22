# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(start, duration, idx) for idx, (start, duration) in enumerate(tasks)]
        tasks.sort() 

        heap = []  
        ans = []
        n = len(tasks)
        time = 0
        i = 0

        while i < n or heap:
            if not heap:
                time = max(time, tasks[i][0])

            while i < n and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                duration, idx = heapq.heappop(heap)
                ans.append(idx)
                time += duration

        return ans