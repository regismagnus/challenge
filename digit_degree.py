'''
Let's define digit degree of some positive integer as the number of times we need to replace
this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
'''
def digitDegree(n):
    c=0
    n=str(n)
    while len(n)>1:
        c+=1
        s=0
        for char in n:
            s+=int(char)
        n=str(s)
    return c
print(digitDegree(154651099))