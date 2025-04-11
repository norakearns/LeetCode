class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

        You may return the answer in any order.

        Input: n = 4, k = 2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        """

        output = []

        def backtrack(start, comb):
            if len(comb) == k:
                output.append(comb.copy())
                return

            for i in range(start, n+1): # 2-4
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1,[])

        return output