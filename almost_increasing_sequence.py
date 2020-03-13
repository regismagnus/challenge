'''
Given a sequence of integers as an array, 
determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately,
you can remove 2 to get the strictly increasing sequence [1, 3].
'''
def almostIncreasingSequence(sequence):
    n=len(sequence)
    removed=False
    i=0
    while i<n-removed-1:
        if(sequence[i]>=sequence[i+1]):
            if removed:
                return False
            else:
                removed=True
                if i>0 and (sequence[i-1]>=sequence[i+1] or (i>=n-2 or sequence[i]<sequence[i+2])):
                    del sequence[i+1]
                else:
                    del sequence[i]
                i-=1
        i+=1    
    return True
print(almostIncreasingSequence([1, 30, 2, 3]))#True
print(almostIncreasingSequence([1, 3, 2, 1]))#False
print(almostIncreasingSequence([1, 2, 5, 3, 5]))#True
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))#True
print(almostIncreasingSequence([1, 2, 1, 2]))#False
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))#True