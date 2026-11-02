class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One Pass
        prevMap = {} # val -> index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []

        # Two Pass

        # indicies = {} # val -> index

        # # Iterate over to add everything to dict
        # for i,n in enumerate(nums):
        #     indicies[n] = i

        # # Iterate again to calculate compliment
        # for i,n in enumerate(nums):
        #     diff = target - n
        #     if diff in indicies and i != indicies[diff]: # Don't use the same element twice
        #         return [i, indicies[diff]]
        # return []