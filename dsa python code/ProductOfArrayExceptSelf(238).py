class Solution:
    def productExceptSelf(nums):

        pro = [1]*len(nums)
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            pro[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            pro[i] *= suffix
            suffix *= nums[i]

        return pro
        