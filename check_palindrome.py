'''
Given the string, check if it is a palindrome. (A palindrome is a string that reads the same left-to-right and right-to-left.)

Example

For inputString = "aabaa", the output should be true;
For inputString = "abac", the output should be false;
For inputString = "a", the output should be true.
'''
def checkPalindrome(inputString):
    n=len(inputString)-1
    for i in range(0,int(n/2)+1):
        if inputString[i]!=inputString[n-i]:
            return False
    return True

print(checkPalindrome("abac"))