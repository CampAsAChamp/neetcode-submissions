class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use 3 sets: one for rows, columns, boxes
        rows = defaultdict(set) # Row 0 -> {1, 2, 3} | Row 1 -> {4, 5} ...
        cols = defaultdict(set) # Col 0 -> {1, 4, 5 7} | Col 1 -> {2, 9} ...
        boxes = defaultdict(set) # Box (0,0) -> {1, 2, 4, 9, 8} | Box (0, 1): {5, 3} ...

        for r in range(9):
            for c in range(9):
                currSquare = board[r][c]

                # Skip empty squares
                if currSquare == ".":
                    continue

                # Value is a tuple (0,0) or (1, 3) for easy indexing
                boxesKeyTuple = (r // 3, c // 3)

                # If in one of the sets already, then we've seen it before, return false
                if (currSquare in rows[r] or
                    currSquare in cols[c] or
                    currSquare in boxes[boxesKeyTuple]):
                    return False

                # Else add it to the sets
                rows[r].add(currSquare)
                cols[c].add(currSquare)
                boxes[boxesKeyTuple].add(currSquare)

        return True