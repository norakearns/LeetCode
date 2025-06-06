class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        """
        candidates.sort()
        res = []

        def comb(curr,start,target):
            if target == 0:
                res.append(curr)
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                comb(curr + [candidates[i]], i, target - candidates[i])
            return
        comb([], 0, target)
        return res