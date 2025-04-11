class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        """
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)-len(needle) + 1):
            r = i + len(needle)
            substr = haystack[i:r]
            if substr == needle:
                return i
        return -1 # base case