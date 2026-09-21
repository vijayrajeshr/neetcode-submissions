class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two pointers
        max_profit = 0
        left = 0
        minbuy = prices[0] # buying on first day
        

        for sell in prices:
            max_profit = max(max_profit,sell - minbuy)
            minbuy = min(sell,minbuy)
        return max_profit 


