'''
After the candy store, Tom and Uri stop by a skate park. Neither knows how to skateboard 
very well though, so to start out they decide to try just riding the board without pushing.

For the first ride, Tom chooses a route with N check-points, all at varying heights. 
The skateboard\'s speed increases by 1 unit when travelling from high ground to lower ground,
and vice-versa, its speed decreases by 1 unit when travelling from low ground to higher ground.

Uri calculates in her head what is the maximum speed Tom will achieve on each route. 
It is given that the skateboard starts at checkpoint 1 and its initial speed is 1.

input
4
15 12 31 30
'''
import sys

N = int("4")
H = map(int, "15 12 31 30".split())
if (sys.version_info > (3, 0)):
     # Python 3 - convert to list
     H = list(H) 
m = s = 1
for i in range(N-1):
    if H[i] > H[i+1]:
        s +=1
        if s > m:
            m = s
    elif H[i] != H[i+1]:
        s -= 1
print(m)