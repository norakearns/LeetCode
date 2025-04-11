class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

        Input: s = "abc", t = "ahbgdc"
        Output: true
        """

        sp = 0
        tp = 0
        if s == "":
            return True

        else:
            while tp < len(t) and sp < len(s):
                if s[sp] == t[tp]:
                    sp += 1
                    tp += 1
                else:
                    tp += 1
            if sp == len(s):
                return True
        return False