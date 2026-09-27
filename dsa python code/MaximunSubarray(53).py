class Solution:
    def maxSubArray(nums):
        sum = float('-inf')
        cur  = 0
        for i in nums:
            cur += i
            if cur > sum:
                sum = cur
            if cur <0:
                cur = 0

        return sum
        