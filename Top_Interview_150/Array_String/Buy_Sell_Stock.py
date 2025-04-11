class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        """

        b = 0
        s = 1
        max_profit = 0 # 5

        while s < len(prices):
            profit = prices[s] - prices[b] # profit = 5 - 1
            if profit < 0:
                b = s 
            else:
                max_profit = max(profit, max_profit) 
            s += 1
        return max_profit