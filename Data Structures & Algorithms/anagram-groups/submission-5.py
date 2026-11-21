class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # charCounter -> [rawStrs]
        sortedStrs = defaultdict(list)

        for s in strs:
            charCounter = [0] * 26
            for c in s:
                charCounter[ord(c) - ord('a')] += 1
            key = tuple(charCounter)
            
            sortedStrs[key].append(s)

        return list(sortedStrs.values())