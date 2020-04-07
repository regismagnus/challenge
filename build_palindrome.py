'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
'''
def buildPalindrome(st):
    end=""
    i=0
    while st+end!=(st+end)[::-1] and i<len(st):
        end=st[i]+end
        i+=1
    return st+end
print(buildPalindrome('abcdc'))