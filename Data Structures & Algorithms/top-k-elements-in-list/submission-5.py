class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each number appears
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create a list of empty lists. freq[i] = all the numbers that appear i times
        # len(nums) + 1, because the max number of times a num can appear is len(nums) -- if the array was all a single number
        # Indexes go from [0 - len(nums)], so we need len(nums) + 1
        # Index 0 is never used, since every number in nums will appear at least once, you can't appear in nums 0 times
        freq = [[] for i in range(len(nums) + 1)]

        # Fill the buckets
        # freq[3] = 1 ; because 1 occurs 3 times
        for num, cnt in count.items():
            freq[cnt].append(num)
        # Result
        # freq = [[], [3], [2], [1], [], [], []]
        # freq is now implicitly sorted by frequency

        # Collect the top k
        res = []
        # range(len(freq) - 1, 0, -1)
        # start = len(freq) - 1
        # stop = 0 (not included)
        # step = -1
        for i in range(len(freq) - 1, 0, -1): # This line walks the buckets backwards, so we visit the most frequent numbers first
            # Go through every number in the current bucket and append it to the answer array
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res