class Solution:
    def isSafe(self, row, col, board, value):
        n = len(board)
        
        for i in range(n):
            # row check
            if board[row][i] == value:
                return False
            
            # col check
            if board[i][col] == value:
                return False
            
            # 3*3 box check
            if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == value:
                return False
        
        return True
    
    def solve(self, board):
        n = len(board)
        
        for i in range(n):
            for j in range(n):
                # check for empty cell
                if board[i][j] == 0:
                    # try to fill with values ranging from 1 to 9
                    for val in range(1, 10):
                        # check for safety
                        if self.isSafe(i, j, board, val):
                            # insert
                            board[i][j] = val
                            # recursion will handle the rest
                            if self.solve(board):
                                return True
                            else:
                                # backtrack
                                board[i][j] = 0
                    # if no value from 1 to 9 works, return False
                    return False
        # all cells filled
        return True
    
    def SolveSudoku(self, grid):
        return self.solve(grid)
    
    def printGrid(self, grid):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
            print()


# Taking input and calling the solution
t = int(input())
for _ in range(t):
    grid = []
    for i in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    
    ob = Solution()
    
    if ob.SolveSudoku(grid):
        ob.printGrid(grid)
    else:
        print("No solution exists")
