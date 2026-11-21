class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Iterate over every string
        # Sort the string
        # Keep a map of {sortedStr → [strs]}

        sortedMap = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            sortedMap[sorted_str].append(s)

        toReturn = list(sortedMap.values())
        return toReturn