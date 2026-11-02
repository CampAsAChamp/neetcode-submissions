class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Built In Python set
        return len(set(nums)) < len(nums)


        # # Manual with Set
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        # return False