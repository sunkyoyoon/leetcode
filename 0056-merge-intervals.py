class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(len(intervals)):
            if res == []:
                res.append(intervals[i])
                continue 
            interval1 = res[-1]
            interval2 = intervals[i]

            if interval1[1] < interval2[0]:
                res.append(interval2)
                continue
            
            if interval1[1] >= interval2[0]:
                res.pop()
                res.append([min(interval1[0], interval2[0]), max(interval1[1], interval2[1])])
        
        return res
