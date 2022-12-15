class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_prof = 0
        for price in prices[1:]:
            min_val = min(min_val, price)
            max_prof = max(price-min_val, max_prof)
        return max_prof
