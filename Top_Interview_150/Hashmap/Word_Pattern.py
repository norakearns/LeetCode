class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word, and no two words map to the same letter.

        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true
        """

        p_list = list(pattern)
        s_list = s.split(' ')

        if len(p_list) != len(s_list):
            return False

        psDict = {} # {a: dog, b: cat}
        spDict = {} # {dog: a, cat: b}

        for i in range(len(p_list)):
            if p_list[i] in psDict and psDict[p_list[i]] != s_list[i]:
                return False
            if s_list[i] in spDict and spDict[s_list[i]] != p_list[i]:
                return False
            psDict[p_list[i]] = s_list[i]
            spDict[s_list[i]] = p_list[i]
        
        return True