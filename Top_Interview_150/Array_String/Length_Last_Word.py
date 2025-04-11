class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of words and spaces, return the length of the last word in the string.

        A word is a maximal substring consisting of non-space characters only.

        Input: s = "Hello World"
        Output: 5
        """
        
        s = s.strip()
        s_arr = s.split(' ')
        length = len(s_arr[-1])
        return length