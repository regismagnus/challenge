'''
Find a pair of magic numbers those tie themselves together
Like husband and wife, numbers in the law of univer has some pair tie to itselves call Amicable numbers. 
They are two different numbers a and b so related that the sum of the proper divisors of a is equal to the proper divisors of b.
A proper divisor of a number is a positive integer divisor other than the number itself.
If a is equal b, they are called perfect number. 
Take an example, 220 and 284, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110,
of which the sum is 284; and the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.
Your mission is to write a piece of script, to find the pair of given input. Output the amicable pair number if exists,
if not, output "NONE". If the number is perfect, output "PERFECT". Sample input 220 Output 284

Upgrade
The divisors of 100 are: 
1 2 4 5 10 20 25 50 100

If we look carefully, all the divisors are present in pairs.
For example if n = 100, then the various pairs of divisors are: (1,100), (2,50), (4,25), (5,20), (10,10)
'''
import math
def sob(n):
    sum=0 
    i=1
    while i <= int(math.sqrt(n)):     
        if (n%i==0):
            sum +=i 
            if (i!=1 and n/i!=i) : 
                 sum+=n/i 
        i+=1
    return sum
a=int(100485)
b=sob(a)
if a==b:
    print("PERFECT")
else: 
    if a == sob(b):
        print(b)
    else:
        print("NONE")