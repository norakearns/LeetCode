class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

        Input: nums = [3,2,3]
        Output: 3
        """
        nums.sort()
        med_index = len(nums)//2
        return(nums[med_index])