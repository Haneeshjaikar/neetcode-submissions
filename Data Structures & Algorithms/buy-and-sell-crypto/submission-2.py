class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        max_profit = 0
        while r>l:
            if prices[l+1] < prices[l]:
                l+=1
                continue
            if prices[r-1] > prices[r]:
                r-=1
                continue
            for i in range(r, l-1, -1):
                max_profit = max(max_profit, prices[r] - prices[i])
            r-=1
            continue
        return max_profit
            
        