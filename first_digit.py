'''
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be
firstDigit(inputString) = '2';
For inputString = "0ss", the output should be
firstDigit(inputString) = '0'.

best solution by andrew_pudge:
    return re.findall('\d', inputString)[0]
'''
def firstDigit(inputString):
    return [i for i in inputString if i.isdigit()][0]
print(firstDigit("asad23asds"))