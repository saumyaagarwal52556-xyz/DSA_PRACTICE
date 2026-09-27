class Solution:
    def maximumDifference(nums):

        maxi = -1
        mini = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > mini :
                maxi = max(maxi , nums[i] - mini)
            else:
                mini = nums[i]
        
        return maxi
        