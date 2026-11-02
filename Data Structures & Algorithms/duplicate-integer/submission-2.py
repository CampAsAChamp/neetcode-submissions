class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Built In Python set constructor which removes duplicates
        # If set is smaller, return true because duplicates must have been removed
        return len(set(nums)) < len(nums)

        # # Manual with Set
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        # return False