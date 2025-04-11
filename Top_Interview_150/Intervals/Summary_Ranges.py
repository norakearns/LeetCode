class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        You are given a sorted unique integer array nums.

        A range [a,b] is the set of all integers from a to b (inclusive).

        Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

        Each range [a,b] in the list should be output as:

        "a->b" if a != b
        "a" if a == b

        Input: nums = [0,1,2,4,5,7]
        Output: ["0->2","4->5","7"]
        """
        output = []

        if not nums: # check if empty
            return output
        
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]

        if start == nums[-1]:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(nums[-1]))

        return output