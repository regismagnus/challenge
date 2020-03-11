'''
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
'''
def rotateImage(a):
    l=len(a)
    return [[a[(l-1)-x][y] for x in range(l)] for y in range(l)]
    
print(rotateImage([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]))