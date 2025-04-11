from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        """

        dic = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            dic[sorted_word].append(word)

        return [val for val in dic.values()]