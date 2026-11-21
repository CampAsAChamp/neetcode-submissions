class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass, building the hash map as we go
        indexes = {}
        for i,n in enumerate(nums):
            compliment = target - n

            if compliment in indexes:
                return [indexes[compliment], i]
            
            else: # Else add it
                indexes[n] = i