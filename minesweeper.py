'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain 
a mine have a number in it that indicates the total number of mines in the neighboring cells. 
Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
'''
def minesweeper(matrix):
    row_l=len(matrix)
    col_l=len(matrix[0])
    
    matrix_r=[[ 0 for i in range(col_l)] for b in range(row_l)]
    for i in range(row_l):
        for b in range(col_l):
            for c in [1, 0, -1]:
                for d in [1, 0, -1]:
                    if i+c>-1 and i+c<row_l and b+d>-1 and b+d<col_l and (c!=0 or d!=0):
                        matrix_r[i][b]+=int(matrix[i+c][b+d])
    return matrix_r
    
true=True
false=False
print(minesweeper([[true,false,false], 
                  [false,true,false], 
                  [false,false,false]]))