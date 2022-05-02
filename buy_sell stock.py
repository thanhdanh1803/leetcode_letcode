class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        else:
            for i in range(n - 1):
                prices[i] = prices[i+1] - prices[i]
            prices[n-1] = 0
            profit = 0
            profit_step = -1
            for step in prices:
                if profit_step <= 0:
                    if step < 0:
                        continue
                    else:
                        profit_step = step
                else:
                    profit_step += step
                
                if profit_step > profit:
                    profit = profit_step
        return profit
            