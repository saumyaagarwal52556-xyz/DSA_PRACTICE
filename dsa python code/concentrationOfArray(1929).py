def getConcatenation(nums):
        n=len(nums)
        ans = [1]* len(nums)*2  

        for i in range(n):
            ans[i] = nums[i] 
            ans[n+i ] = nums[i]

        return ans