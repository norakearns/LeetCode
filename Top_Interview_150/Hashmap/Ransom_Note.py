class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

        Each letter in magazine can only be used once in ransomNote.

        Input: ransomNote = "a", magazine = "b"
        Output: false
        """

        magMap = {}
        for char in magazine:
            if char in magMap:
                magMap[char] += 1
            else:
                magMap[char] = 1

        for letter in ransomNote:
            if letter not in magMap:
                return False
            else:
                if magMap[letter] == 0:
                    return False
                magMap[letter] -= 1

        return True
