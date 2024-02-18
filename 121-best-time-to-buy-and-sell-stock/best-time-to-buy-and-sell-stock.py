# REACTO - https://www.youtube.com/watch?v=DIR_rxusO8Q&t=87s 
# Repeat - Given a list of stock price, find the max profit you can make. 
# Clarifying questions - 1. Can you sell before you buy? 2. Can you have 0 profits? 
# Examples - 1. [1,4,7] -> 6, [6,5,1] -> 0, [1] -> 0, [] -> 0
# Approach -   1. 
# find minimum value, keep max_profit, return the value -> Complexity O (n)
# Code
# Test
# Optimisation

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf') 
        max_profit = 0
        for price in prices: # Testing - [1,4,7], [6,5,1], [1], []
            if price < min_price: 
                min_price = price # Testing - [1, 1, 1], [6,5,1], [1]
            
            temp_max_profit =  price - min_price # Testing = [0,3,6], [0, -1, -5], [0]
            if temp_max_profit > max_profit:
                max_profit = temp_max_profit # Testing = [0,3,6], [0,0,0], [0]

        return max_profit # returns 0 for empty list
           