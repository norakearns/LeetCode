class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string s, reverse the order of the words.

        A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

        Return a string of the words in reverse order concatenated by a single space.

        Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

        Input: s = "the sky is blue"
        Output: "blue is sky the"
        """
        s_stripped = s.strip()
        s_arr = s_stripped.split()
        res = s_arr[-1]

        for i in range(len(s_arr)-2, -1, -1):
            res = res + " " + s_arr[i]

        return res