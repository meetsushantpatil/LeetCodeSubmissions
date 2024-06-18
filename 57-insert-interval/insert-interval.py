class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        # if both new _start & new_end, falls before the starting element, insert at the start
        # if new_start falls in an interval & new_end falls within the same, extend the current interval.
        # if new_start falls in an interval & new_end falls within another, merge all of the subsequent intervals.
        # if both fall outside of overall range, insert at the end.

        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i+=1
        merged.append(newInterval)

        while i < len(intervals):
            merged.append(intervals[i])
            i+=1

        return merged


                
                

                
