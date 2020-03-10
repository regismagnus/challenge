'''
inputs ex
aaabcccdeeef
abcbad
abcabcabc
aabbc
'''
input="aabbc"
n=len(input)
i=0
while i<n:
    is_next_same=i<(n-1) and input[i]==input[i+1]
    if not is_next_same and (i==0 or input[i]!=input[i-1]):
        print(input[i])
        exit()
    if is_next_same:
        i+=1
    i+=1
print("NONE")