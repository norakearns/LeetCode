class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        """
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            lp = i+1 
            rp = len(nums) - 1 
            while lp < rp:
                total = nums[i] + nums[lp] + nums[rp] 
                if total > 0:
                    rp -= 1 
                elif total < 0:
                    lp += 1
                else:
                    res.append([nums[i], nums[lp], nums[rp]])
                    lp += 1 # 3
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1
        
        return res