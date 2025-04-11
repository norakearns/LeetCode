class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, or false otherwise.

        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        """

        s_alnum = ""

        for char in s:
            if char.isalnum():
                s_alnum += char.lower()

        l = 0
        r = len(s_alnum) - 1

        while l < r:
            if s_alnum[l] != s_alnum[r]:
                return False
            else:
                l += 1
                r -= 1

        return True