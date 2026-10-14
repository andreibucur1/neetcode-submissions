class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        maxdif = 0
        while j < len(prices):
            if prices[i] <= prices[j]:
                maxdif = max(prices[j] - prices[i], maxdif)
                j += 1
            else:
                i = j
                j += 1
        return maxdif
