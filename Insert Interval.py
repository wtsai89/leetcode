from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i += 1 
        
        if i == len(intervals):
            return intervals + [newInterval]
        if newInterval[1] < intervals[i][0]:
            intervals.insert(i, newInterval)
            return intervals
        
        if newInterval[0] < intervals[i][0]:
            intervals[i][0] = newInterval[0]
        if newInterval[1] > intervals[i][1]:
            intervals[i][1] = newInterval[1]
        newInterval = intervals[i]
        i += 1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            if intervals[i][1] > newInterval[1]:
                newInterval[1] = intervals[i][1]
            intervals.pop(i)

        return intervals

s = Solution()
print(s.insert([[1,3],[6,9]],[2,5]))