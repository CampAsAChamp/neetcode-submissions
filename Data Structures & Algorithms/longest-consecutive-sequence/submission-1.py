class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add them to a set and traverse the set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Reset
            if (num-1) not in numSet:
                length = 1
            # Keep checking
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest