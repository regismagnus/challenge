'''
Calculate the product of two big integers
'''
def mult(a, b):
    al=len(a)
    bl=len(b)
    
    if a=="0" or b=="0" or al==0 or bl==0:
        return "0"

    r=["" for i in range(al)]
    
    res=0
    for i in range(al-1, -1, -1):
        for i2 in range(bl-1, -1, -1):
            aux=str(int(a[i])*int(b[i2])+res)
            r[i]=aux[len(aux)-1]+r[i]
            if len(aux)>1:
                res=int(aux[0])
            else:
                res=0
        if res>0:
            r[i]=str(res)+r[i]
            res=0
    
    r_f=r[al-1]
    for i in range(al-2, -1, -1):
        d=len(r[i])-(al-i)+1
        r_f=sum(r_f, r[i]+("0"*(len(r[i])-d)))
    return r_f;

def sum(a, b):
    r=""
    al=len(a)
    bl=len(b)
    if al>bl:
        max=al
    else: 
        max=bl           
    
    res=0    
    for i in range(0, max):
        aux=res
        if al> i and a[al-1-i]:
            aux+=int(a[al-1-i])
        if bl> i and b[bl-1-i]:
            aux+=int(b[bl-1-i])
        
        aux=str(aux)
        r=aux[len(aux)-1]+r
        if len(aux)>1:
            res=int(aux[0])
        else:
            res=0
    if res>0:
        r=str(res)+r
    return r

b="654154154151454545415415454"
a="63516561563156316545145146514654"
    
print(mult(a, b))