class Solution:
    def encode(self, strs: List[str]) -> str:
        # Check whether the list is empty
        # Use `if not strs:` instead of `len(strs) == 0`
        # - Is shorter
        # - Works on anything with truthiness, not just things with a length: 
        #     None, 
        #     0, 
        #     "", 
        #     empty dicts and sets, and so on. 
        # - len(None) raises a TypeError, while not None just returns True.
        if not strs:
            return ""

        # Create an array with the sizes
        sizes = [len(s) for s in strs]

        # Add the sizes to the front of the string
        res = []
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#') # Mark the end of the size section

        # Stitch/concats the all the strings together in the array
        res.extend(strs)

        # Turn that array into a string
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res