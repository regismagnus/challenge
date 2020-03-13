'''
After becoming famous, the CodeBots decided to move into a new building together.
Each of the rooms has a different cost, and some of them are free,
but there's a rumour that all the free rooms are haunted!
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms,
or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room,
your task is to return the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.

There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For

matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
the output should be
matrixElementsSum(matrix) = 9.

Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it).
Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
'''
def matrixElementsSum(matrix):
    s=0
    c_z=[False for i in range(len(matrix[0]))]
    for i in range(0, len(matrix)):
        for b in range(0, len(matrix[i])):
            if not c_z[b] and matrix[i][b]!=0 and (i==0 or matrix[i-1][b]!=0):
                s+= matrix[i][b]
            else:
                c_z[b]=True
    return s
print(matrixElementsSum([[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]))