'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

Example

For cell = "a1", the output should be
chessKnight(cell) = 2.

For cell = "c2", the output should be
chessKnight(cell) = 6.
'''
def chessKnight(cell):
    cols='abcdefgh'
    c=cols.find(cell[0])+1
    l=int(cell[1])
    
    moves=8
    if c+1>8 or l+2>8:
        moves-=1
    if c+2>8 or l+1>8:
        moves-=1
    if c-1<1 or l+2>8:
        moves-=1    
    if c-2<1 or l+1>8:
        moves-=1
    
    if c+1>8 or l-2<1:
        moves-=1
    if c+2>8 or l-1<1:
        moves-=1
    if c-1<1 or l-2<1:
        moves-=1    
    if c-2<1 or l-1<1:
        moves-=1
    return moves
print(chessKnight('a1'))