class Solution(object):
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isRowValid(board):
            for i in range(9):
                checkRow={}
                for j in range (9):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in checkRow:
                        return False
                    checkRow[board[i][j]]=board[i][j]
            return True
        
        def isColumnValid(board):
            for j in range(9):
                checkColumn={}
                for i in range (9):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in checkColumn:
                        return False
                    checkColumn[board[i][j]]=board[i][j]
            return True
        
        def isBoardValid(board,n=0,m=0):
            checkBoard={}
            for i in range(n,n+3):
                for j in range(m,m+3):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in checkBoard:
                        return False
                    checkBoard[board[i][j]]=board[i][j]
            if m!=6:
                return isBoardValid(board,n,m+3)
            if n!=6:
                return isBoardValid(board,n+3,m=0)
            return True                               
        
        if isRowValid(board) and isColumnValid(board) and isBoardValid(board):
            return True
        return False

board=[[".",".",".",".",".",".","5",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
["9","3",".",".","2",".","4",".","."],
[".",".","7",".",".",".","3",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".","3","4",".",".",".","."],
[".",".",".",".",".","3",".",".","."],
[".",".",".",".",".","5","2",".","."]]
a=Solution()
a.isValidSudoku(board)