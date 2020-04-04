'''
Given the positions of a white bishop and a black pawn on the standard chess board,
determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false

best solution by chris_r53 in C#:
    return Math.Abs(b[0]-p[0])==Math.Abs(b[1]-p[1]);
'''
def bishopAndPawn(bishop, pawn):
    cols=['a','b','c','d','e','f','g','h']
    cb=cols.index(bishop[0])+1
    rb=int(bishop[1])
    cp=cols.index(pawn[0])+1
    rp=int(pawn[1])
    m=0
    while m+cb<9 or cb-m>0:
        m+=1
        if (cb+m==cp and rb+m==rp) or (cb-m==cp and rb+m==rp) or (cb+m==cp and rb-m==rp) or (cb-m==cp and rb-m==rp):
            return True
    return False
print(bishopAndPawn('', ''))