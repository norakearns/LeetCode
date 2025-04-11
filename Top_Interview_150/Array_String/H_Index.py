class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

        According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

        Input: citations = [3,0,6,1,5]
        Output: 3
        """
        citations.sort()
    
        n = len(citations)
        
        for i in range(n): # i = 0
            h = n - i # h = 3
            if citations[i] >= h:
                return h
        
        return 0