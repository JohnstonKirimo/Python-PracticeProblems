"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0:return 0
        costs = [1001]*k
        profits = [0]*k

        for p in prices:
            cash = 0
            for i in range(k):
                costs[i] = min(costs[i],p-cash)
                profits[i] = max(profits[i],p-costs[i])
                cash = profits[i]

        return profits[-1] if k != 0 else 0
        
