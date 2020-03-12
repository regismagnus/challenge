'''
Sam found N rings of varying radiuses in the market. 
He arranged them on the floor so that each ring (except the first and last) touches the ones before and after it.

He started turning the first ring and noticed that the other rings turned as well; some faster, some slower!
Help Sam to count how many times the other rings turn while the first ring turns once.

INPUT
The first line of input contains an integer N (3 ≤ N ≤ 100), 
the number of rings. The next line contains N integers between 1 and 1000, the radiuses of Sam rings, 
in the order they are laid out on the floor.

OUTPUT
The output must contain N-1 lines. For every ring other than the first, in the order they are given in the input,
output a fraction A/B, meaning that the respective ring turns A/B times while the first ring turns once.
The fractions must be in reduced form (the numerator and denominator must not have a common divisor larger than 1).
'''
n=int("5")
r=map(int, "16 676 766 611 73".split())

for i in range(1, n):
    f=1
    rf=r[0]/r[i]
    while (r[0]*f)%r[i]!=0:
        f+=1
        rf=r[0]*f/r[i]
    print(str(rf)+"/"+str(f))