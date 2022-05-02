class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0,len(prices)-1):
            change = prices[i+1] - prices[i]
            if(change>0):
                profit+=change
        return profit