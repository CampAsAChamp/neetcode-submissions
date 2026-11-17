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

        header_end = s.index('#')
        header = s[:header_end]

        sizes = []
        # for part in header.split(','):
        #     if part:  # skip the empty piece after the trailing comma
        #         sizes.append(int(part))

        # List comprehension version
        # `if n` filters the empty string left by the trailing comma in the header ("4,3,#" splits into ['4', '3', '']).
        sizes = [int(n) for n in header.split(',') if n] 

        res = []
        start = header_end + 1 # Start is the start of the strings/chars
        for size in sizes:
            # Extract string
            substr = s[start:start + size]
            res.append(substr)

            # Move to the next one
            start += size
        return res