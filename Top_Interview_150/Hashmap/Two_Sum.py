class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        """

        numMap = {}

        for i, num in enumerate(nums): # i = 1, num = 7
            complement = target - num # comp = 2
            if complement in numMap:
                return [numMap[complement], i]
            else:
                numMap[num] = i