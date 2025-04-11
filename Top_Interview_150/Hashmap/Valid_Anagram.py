class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        Input: s = "anagram", t = "nagaram"
        Output: true
        """

        if len(s) != len(t):
            return False
        
        sMap = {}

        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1

        for char in t:
            if char not in sMap or sMap[char] == 0:
                return False
            else:
                sMap[char] -= 1

        return True