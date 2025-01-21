class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        price_min = prices[0]

        for i in range(len(prices)):
            profit = 0
            if prices[i] < price_min:
                price_min = prices[i]
            if prices[i] > price_min:
                if i > prices.index(price_min):
                    profit = prices[i] - price_min
                    profit_list.append(profit)

        if not profit_list: return 0
        return max(profit_list)