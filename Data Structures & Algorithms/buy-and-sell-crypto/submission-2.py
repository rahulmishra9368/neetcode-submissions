class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        i = 0
        j = 1
        while i <j and j < len(prices):
            if prices[j] < prices[i]:
                buy = prices
                i = j
            if prices[j] - prices[i] > sell:
                print(prices[j] - prices[i] )
                sell = prices[j] - prices[i]
            j += 1
        return sell


        