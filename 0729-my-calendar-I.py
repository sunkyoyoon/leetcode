class MyCalendar:

    def __init__(self):
        self.time = [] 

    def book(self, startTime: int, endTime: int) -> bool:
        left = 0 
        right = len(self.time)
        while left < right:
            mid = (left + right) // 2
            interval = self.time[mid]
            start = interval[0]
            end = interval[1]
            if endTime > start and startTime < end:
                return False
            if startTime >= end:
                left = mid + 1 
            else:
                right = mid
        self.time.insert(left, [startTime, endTime])
        return True 



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
