class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currentSquare = board[r][c]
                if currentSquare == ".":
                    continue
                if (currentSquare in rows[r]
                    or currentSquare in cols[c]
                    or currentSquare in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(currentSquare)
                rows[r].add(currentSquare)
                squares[(r // 3, c // 3)].add(currentSquare)

        return True