class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],x[1]))
        interval1 = intervals[0]

        ans = 0 
        for i in range(1,len(intervals)):
            interval2 = intervals[i]
            if interval2[0] < interval1[1]:
                ans += 1 
                interval1 = [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
            else:
                interval1 = interval2
        return ans



