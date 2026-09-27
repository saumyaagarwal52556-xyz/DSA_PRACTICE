class Solution:
    def twoSum(nums, target):
        
        seen = {}
        for i in range(len(nums)):
            req = target - nums[i]

            if req in seen:
                return [seen[req],i]

            seen[nums[i]] = i
        return []