'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_profit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_profit=max(max_profit.profit)
            else:
                l=r
        return max_profit
'''
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


        