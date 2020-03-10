'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
'''
def firstNotRepeatingCharacter(s):
    l={}
    for i in range(0,len(s)):
        if s[i] in l:
            l[s[i]]+=1
        else:
            l[s[i]]=1
    print(l)       
    for i in l:
        if l[i]==1:
            return i
    return '_'
print(firstNotRepeatingCharacter('z'))