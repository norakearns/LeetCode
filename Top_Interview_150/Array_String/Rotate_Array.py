class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        """
        k = k % len(nums)
        i = 0
        while i < k:
            temp = nums.pop()
            nums.insert(0, temp)
            i += 1
        return nums