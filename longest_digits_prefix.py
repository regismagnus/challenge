'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

best solution by thienbui:
    return re.findall('^\d*',inputString)[0]
'''
def longestDigitsPrefix(inputString):
    i=0
    while i<len(inputString) and inputString[:i+1].isdigit():
        i+=1
    return inputString[:i] if i>0 else ""
print(longestDigitsPrefix("123aa1"))