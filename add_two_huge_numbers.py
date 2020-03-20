'''
You're given 2 huge integers represented by linked lists.
Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits.
The represented number might have leading zeros.
Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.
'''
# Singly-linked lists are already defined with this interface:
class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def addTwoHugeNumbers(a, b):
    c=a
    s1=""
    while c:
        c.value = str(c.value);
        while len(c.value)<4:
            c.value="0"+c.value            
        s1 += c.value
        c=c.next
        
    c=b;
    s2=""
    while c:
        c.value = str(c.value)
        while len(c.value)<4:
            c.value="0"+c.value            
        
        s2 += c.value
        c=c.next
        
    r = str(int(s1)+int(s2))
    
    ra=[0]
    ra[0]=""
    
    for i in range(len(r)-1, -1, -1):
        if len(ra[0])==4:
            ra[0]=int(ra[0])
            ra.insert(0, "")

        ra[0] = r[i]+ra[0]
        
    ra[0]=int(ra[0])
    
    return ra
 
    
a=ListNode(123);
a.next=ListNode(4);
a.next.next=ListNode(5);

b=ListNode(100);
b.next=ListNode(100);
b.next.next=ListNode(100);
print(addTwoHugeNumbers(a,b))