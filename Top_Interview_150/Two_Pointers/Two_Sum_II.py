class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        """
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            total = numbers[lp] + numbers[rp]
            if total == target:
                return [lp+1, rp+1]
            elif total > target:
                rp -= 1
            else:
                lp += 1