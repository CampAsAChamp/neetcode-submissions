class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sortedStr -> rawStr
        strMap = defaultdict(list)

        # Iterate over all the strs and add each sorted
        for s in strs:
            sortedStr = "".join(sorted(s))
            # Add/append the raw strip to the list in the map with
            strMap[sortedStr].append(s)

        toReturn = list(strMap.values())
        return toReturn