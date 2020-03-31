'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
'''
def arrayMaxConsecutiveSum(inputArray, k):
    m=s=sum(inputArray[0:k])
    for i in range(1, len(inputArray)-k+1):
        s=s-inputArray[i-1]+inputArray[k+i-1]
        if(m<s):
            m=s
    return m
    #too slow but work
    #return max([sum(inputArray[i:i+k]) for i in range(len(inputArray)-k+1)])
print(arrayMaxConsecutiveSum([3, 2, 1, 1], 1))