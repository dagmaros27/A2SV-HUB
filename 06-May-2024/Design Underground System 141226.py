# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(list)  # userid : [startplace, time] 
        self.averages = defaultdict(list) # (start:end): [times]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id].append(stationName)
        self.check_in[id].append(t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.check_in[id]
        self.averages[(start[0], stationName)].append( t - start[1])
        del self.check_in[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip_times = self.averages[(startStation,endStation)]
        average = sum(trip_times)/len(trip_times)

        return average
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)