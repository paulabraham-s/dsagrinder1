class Solution(object):
    def moveZeroes(self, nums):
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        
        zero_count = len(nums) - len(result)
        result.extend([0] * zero_count)
        
        for i in range(len(nums)):
            nums[i] = result[i]