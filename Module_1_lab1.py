from collections import Counter

def FindDuplicates(string:str) -> bool:
    ''' In this function with the help collection library we find if any duplicate numbers are found'''
    counter = Counter(string)
    duplicates = [letter for letter in counter if counter[letter] > 1]
    if duplicates == ['.']:
        return True
    else:
        return False
def RowValidator(board:list[list]) -> bool:
    '''This function is created for validating the rows '''
    for i in board:
        if FindDuplicates(i):
            continue
        else:
            return False
    return True

def ColumnValidator(board:list[list]) -> bool:
    ''' This function will validate all the columns if the sudoku board and return a boolean value '''
    Columnlist = list()
    for i in range(0,9):
        Colboard = list()
        for j in range(0,9):
            Colboard.append(board[j][i])
        Columnlist.append(Colboard)
    
    for i in Columnlist:
        if FindDuplicates(i):
            continue
        else:
            return False
    return True
def MatrixValidator(board:list[list]) -> bool:
    ''' This function will valide all the 3X3 sub grids and validate them'''
    for i in range(0,9,3):
        for j in range(0,9,3):
            subgrid = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
            if not FindDuplicates(subgrid):
                return False
    return True
def SudokuValidator(board:list[list]):
    '''This function is created for validating a 9X9 sudoku board'''
    print('Yes') if RowValidator(board) & ColumnValidator(board) & MatrixValidator(board) else print('No')
    
    
with open(r'C:\Users\hi\OneDrive\Desktop\VITB notes\Python Self study\litinput.txt',"r") as f:
    board = list(map(lambda x: x.strip(),f.readlines()))
    board = list(map(lambda x: x.split(" "),board))

SudokuValidator(board)
