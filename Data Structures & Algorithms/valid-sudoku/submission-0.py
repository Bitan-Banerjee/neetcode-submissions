class Solution:
    def validRows(self,board):

        for i in range(9):
            # Creat a map for checking repeated values
            map = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue

                # if element is present in map, it means it's duplicate
                if board[i][j] in map or board[i][j] == '0':
                    return False
                
                map[board[i][j]] = 1
        return True


    def validColumns(self,board):
        for j in range(9):
            # Map to check for repeating numbers
            map = {}
            for i in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in map or board[i][j] == "0":
                    return False
                
                map[board[i][j]] = 1
        return True


    def validBox(self,board):
        for i in range(0,8,3):
            for j in range(0,8,3):
                # Map for checking repeating chars in box
                map = {}
                for m in range(i,(i+3)):
                    for n in range(j,(j+3)):
                        if board[m][n] == ".":
                            continue

                        if board[m][n] in map or board[m][n] == "0":
                            return False
                        
                        map[board[m][n]] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if self.validColumns(board) and self.validRows(board) and self.validBox(board):
            return True
        
        return False
        