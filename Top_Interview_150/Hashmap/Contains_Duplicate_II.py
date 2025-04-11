class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

        Input: nums = [1,2,3,1], k = 3
        Output: true
        """
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                dist = abs(numDict[nums[i]] - i)
                if dist <= k:
                    return True
            numDict[nums[i]] = i
        return False
