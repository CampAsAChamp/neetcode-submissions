class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        # Both ends start at 1 because there is nothing to the left of the first number, and nothing to the right of the last number
        pref[0] = suff[n - 1] = 1
        
        # Product of all numbers to the *left* of the current number (prefix pass)
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        # Product of all numbers to the *right* of the current number (suffix pass)
        # Usually to start at the end you would do `n-1`, but since we already know that index to be 1 we skip it
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        # Create output array
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res