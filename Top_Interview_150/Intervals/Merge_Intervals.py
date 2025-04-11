class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        """
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]

        for current in intervals[1:]:
            prev_end = merged[-1]
            curr_start, curr_end = current

            if curr_start <= prev_end:
                merged[-1][1] = max(prev_end, curr_end)
            else:
                merged.append(current)

        return merged