class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two Pass hash table
        # Pass 1: Iterate over nums and add to the dict the index
        
        indexes = {}
        for i,n in enumerate(nums):
            indexes[n] = i

        print("indexes", indexes)

        # Pass 2: Iterate over nums and check if the compliment is in the dict
        for i,n in enumerate(nums):
            compliment = target - n
            print(n, compliment)
            if compliment in indexes and indexes[compliment] != i:
                print("found match", i, indexes[compliment])
                return [i, indexes[compliment]]
        
        return []