class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add them to a set and traverse the set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Check if at the start of the sequence, skip past number if we aren't and are in the middle of a sequence
            if (num-1) not in numSet:
                length = 1
                # Keep checking
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest