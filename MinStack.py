#https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.insert(0,val)

    def pop(self) -> None:
        self.arr.pop(0)

    def top(self) -> int:
        return self.arr[0]

    def getMin(self) -> int:
        return min(self.arr)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.top_ = -1
        self.max = -1

    def push(self, val: int) -> None:
        if self.max == self.top_:
            self.arr += [val]
            self.max+=1
        else:
            self.arr[self.top_+1] = val
        self.top_+=1

    def pop(self) -> None:
        self.top_-=1
        return self.arr[self.top_+1]

    def top(self) -> int:
        return self.arr[self.top_]

    def getMin(self) -> int:
        min = self.arr[self.top_]
        for i in range(self.top_-1,-1,-1):
            if self.arr[i] < min:
                min = self.arr[i]
        return min
            
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()