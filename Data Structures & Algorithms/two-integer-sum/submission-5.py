class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentMap = {}
        for i,currentNum in enumerate(nums):
            compliment = target - currentNum
            if compliment in complimentMap:
                return [complimentMap[compliment], i]
            complimentMap[currentNum] = i
