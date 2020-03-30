'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.

best solution by thienbui:
    return len(set(s))
'''
def differentSymbolsNaive(s):
    count={}
    for w in s:
        if not w in count:
            count[w]=0
        count[w]+=1
    return len(count)

print(differentSymbolsNaive("acbvv"))
