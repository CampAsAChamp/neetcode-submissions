class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        # These squares use the range
        #                   c//3 = 0   c//3 = 1   c//3 = 2
        # r//3 = 0   (0,0)      (0,1)      (0,2)
        # r//3 = 1   (1,0)      (1,1)      (1,2)
        # r//3 = 2   (2,0)      (2,1)      (2,2)

        for r in range(9):
            for c in range(9):
                currentSquare = board[r][c]

                # Skip empty squares
                if currentSquare == ".":
                    continue
                # If we've seen that number before
                if (currentSquare in rows[r]
                    or currentSquare in cols[c]
                    or currentSquare in squares[(r // 3, c // 3)]): # Divide by 3 (floor) to get which box [x,y] we are talking about
                    return False

                # Add the current square to our sets
                cols[c].add(currentSquare)
                rows[r].add(currentSquare)
                squares[(r // 3, c // 3)].add(currentSquare)

        return True