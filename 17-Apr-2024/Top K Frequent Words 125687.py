# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        arr = [(-count, word) for word,count in counter.items()]

        heapify(arr)
        ans = []

        for _ in range(k):
            ans.append(heappop(arr)[1])
            
        return ans


        