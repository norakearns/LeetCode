class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        
        output = []

        digChar = {'2':'abc', '3':'def','4':'ghi',
                '5':'jkl','6':'mno','7':'pqrs', 
                '8':'tuv', '9':'wxyz'}


        def backtrack(i, curStr):
            if len(curStr) == len(digits): # we've built an answer
                output.append(curStr)
                return
            
            for char in digChar[digits[i]]:
                backtrack(i+1, curStr + char)

        if digits:
            backtrack(0, "")

        return output