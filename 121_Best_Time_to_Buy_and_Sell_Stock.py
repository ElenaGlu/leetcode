from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list_digit = []
        final_profit = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    continue
                elif prices[i] < prices[j]:
                    list_digit.append(prices[j])
                diff = max(list_digit, default=0) - prices[i]
                final_profit.append(diff)
                list_digit = []
        return max(final_profit, default=0)


prices = [2,1,2,0,1]  # fix for bigdata
obj = Solution()
print(obj.maxProfit(prices))
