class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if i < j and prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        
        return prices