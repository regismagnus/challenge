# Singly-linked lists are already defined with this interface:
class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def isListPalindrome(l):
    a=convertToArray(l)
    for i in range(int(len(a)/2)):
        if a[i]!=a[len(a)-i-1]:
            return False
    return True
    
def convertToArray(l):
    a=[]
    if(l!=None):
        a.append(l.value)
        c=l.next
        while(c!=None):
            a.append(c.value)
            c=c.next
    return a

'''def count(l):
    b=1
    c=l.next            
    while(c!=None):
       b+=1
       c=c.next
    return b

def getL(i, l):
    if(i==0):
        return l
    c=l.next
    b=1
    while(c!=None):
       if b==i:
           return c
       b+=1
       c=c.next
    return None'''
    
''''l=ListNode(1)
l.next=ListNode(1000000000)
l.next.next=ListNode(-1000000000)
l.next.next.next=ListNode(-1000000000)
l.next.next.next.next=ListNode(1000000000)
l.next.next.next.next.next=ListNode(1)'''
l=ListNode(0)
l.next=ListNode(1)
l.next.next=ListNode(0)
print(isListPalindrome(l))