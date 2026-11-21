class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use 3 sets: one for rows, columns, boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currSquare = board[r][c]

                if currSquare == ".":
                    continue


                # If in one of the sets already, return false
                if (currSquare in rows[r] or
                    currSquare in cols[c] or
                    currSquare in boxes[(r // 3, c // 3)]):
                    return False

                # Else add it to the sets
                rows[r].add(currSquare)
                cols[c].add(currSquare)
                boxes[(r // 3, c // 3)].add(currSquare)
        return True