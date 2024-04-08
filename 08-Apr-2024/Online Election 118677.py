# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.winner = []

        pp = 0
        freq = defaultdict(int)
        for p in persons:
            freq[p] += 1
            if freq[p] >= freq[pp]:
                pp = p
            self.winner.append(pp)
        

    def q(self, t: int) -> int:
        l,h = -1, len(self.times)-1

        while l < h:
            m = (l+h+1)//2

            if self.times[m] <= t:
                l = m 
            else:
                h = m-1
        return self.winner[l]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)