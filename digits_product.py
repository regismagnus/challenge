'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.

'''
def digitsProduct(product):
    if product==0:
        return 10
    i=0
    c=0
    while c<(product*product):
        i+=1
        i_s = str(i)
        c=1
        for b in range(len(i_s)):
            c=int(i_s[b])*c
        if c==product:
            return i
    return -1
print(digitsProduct(12))