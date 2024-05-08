# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        i=0
        j=0
        counter=0
        players.sort()
        trainers.sort()

        while i<len(players) and j<len(trainers):

            if players[i]<=trainers[j]:
                counter+=1
                i+=1
                j+=1
            
            else:
                j+=1
                
        return counter
        