class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequencies
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Build list of [freq, num] pairs so we can sort it
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort() # Sorts by the first number in the pair, and then the second

        # Keep poping from the end of the sorted list (highest frequency) to the answer list, k total times
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res