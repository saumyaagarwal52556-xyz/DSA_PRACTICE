class Solution:
    def maxProfit(prices):
        maxi = 0
        mini = prices[0]

        for i in prices:
            mini = min(mini , i)
            curr = i - mini
            maxi = max(maxi , curr)
        return maxi
        