class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        """
        max_prefix = ""

        for i in range(len(strs[0])):  
            char = strs[0][i]
            print(char)          
            for word in strs[1:]: 
                if i >= len(word) or word[i] != char:
                    return max_prefix           
            max_prefix += char
                
        return max_prefix
