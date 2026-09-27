class Solution:
    def containsDuplicate(nums):
        new = set(nums)
        if len(nums) > len(new):
            return True
        else:
            return False