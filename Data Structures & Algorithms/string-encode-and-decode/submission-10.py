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

    # def decode(self, s: str) -> List[str]:
    #     output = []

    #     # Go through and reconstruct each string since the entire string is of the format `5#Hello5#World`
    #     start = 0
    #     # First find the length of the string
    #     while start < len(s):
    #         end = start # Set the start
    #         # Keep iterating until we find the #, because the length of the string could be double digits
    #         while s[end] != '#':
    #             end += 1 
            
    #         length = int(s[start:end]) # Pull the length out of the string


            
    #         start = end + 1 # Advance to the first actual character and not the #
    #         end = start + length
    #         # Now pull the substring out of the string
    #         substr = s[start:end]
    #         output.append(substr)

    #         start = end

    #     return output