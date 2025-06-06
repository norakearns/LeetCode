class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

        Input: s = "egg", t = "add"
        Output: true
        """
        if len(s) != len(t):
            return False

        stMap = {}
        tsMap = {}
        for i in range(len(s)):
            if s[i] in stMap and stMap[s[i]] != t[i]:
                return False
            if t[i] in tsMap and tsMap[t[i]] != s[i]:
                return False
            stMap[s[i]] = t[i]
            tsMap[t[i]] = s[i]
        
        return True