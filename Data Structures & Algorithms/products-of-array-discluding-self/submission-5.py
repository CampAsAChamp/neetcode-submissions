class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Accumulate
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        
        # Early return if theres more than one zero because it makes everything in the array zero
        if zero_cnt > 1: 
            return [0] * len(nums)

        # Create output array
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res