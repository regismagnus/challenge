'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
'''
def differentSquares(matrix):
    lr = len(matrix)
    lc = len(matrix[0])
    if lr==1 or lc==1:
        return 0
    serials=[]
    count=0

    for r in range(lr-1):
        for c in range(lc-1):
            serial = str(matrix[r][c]) + "_" + str(matrix[r][c+1]) + "_" + str(matrix[r+1][c]) + "_" + str(matrix[r+1][c+1])
            if not serial in serials:
                count+=1
                serials.append(serial)

    return count
print(differentSquares([[1,2,1], 
 [2,2,2], 
 [2,2,2], 
 [1,2,3], 
 [2,2,1]]))