class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        output = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            output.extend(perms)
            nums.append(n)
        return output