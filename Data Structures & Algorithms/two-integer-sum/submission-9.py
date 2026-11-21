class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass, building the hash map as we go
        complimentIndexes = {}
        for i,n in enumerate(nums):
            compliment = target - n

            if compliment in complimentIndexes:
                return [complimentIndexes[compliment], i]
            
            else: # Else add it
                complimentIndexes[n] = i