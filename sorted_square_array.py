'''
You have a sorted array of integers.
Write a function that returns a sorted array containing the squares of those
 integers.

input test
[-7,-3,-1,4,8,12] output [1,9,16,49,64,144]
[1,2,3] output [1,4,9]
[-3,-2,-1] output [1,4,9]
[] output 'INVALID INPUT'
'''
def sortedSquareArray(a):
    return sorted(list(map(lambda x: x*x, a)))
    
print(sortedSquareArray([]))