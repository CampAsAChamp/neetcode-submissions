class Solution:

    def encode(self, strs: List[str]) -> str:
        # One line Python version using f-strings and generator
        return "".join(f"{len(s)}#{s}" for s in strs)

        # output = []
        # for s in strs:
        #     output.append(str(len(s))) # length of the string as first
        #     output.append("#") # Separator
        #     output.append(s) # Actual string content
        
        # # Join everything into one string
        # encodedStr = "".join(output)
        
        # return encodedStr

    def decode(self, s: str) -> List[str]:
        output = []
        start = 0

        while start < len(s):
            delimiter = s.index("#", start)    # find the # after the length
            length = int(s[start:delimiter])

            start = delimiter + 1              # first char of the actual string
            output.append(s[start:start + length])

            start += length                    # jump to the next length prefix

        return output