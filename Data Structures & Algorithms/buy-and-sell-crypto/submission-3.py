class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_buy = prices[0]
        for price in prices:
            max_prof = max((price - min_buy), max_prof)
            min_buy = min(min_buy, price)
        return max_prof            
        