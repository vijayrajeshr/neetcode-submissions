class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            curr_profit = sell-min_buy
            max_profit = max(max_profit,curr_profit)
            min_buy = min(min_buy,sell)
        return max_profit