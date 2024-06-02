# Problem: Design an Ordered Stream - https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.arr = [0 for i in range(n)]
        self.pointer = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        id = idKey -1
        self.arr[id] = value
        if self.pointer < id:
            return []
        else:
            stream = []
            while self.pointer < len(self.arr) and self.arr[self.pointer] != 0 :
                stream.append(self.arr[self.pointer])
                self.pointer += 1
            return stream
       


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)