def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
    
def fibonacci(s,r,n):
    for i in range(n-2):
        s,r=r,s+r
    return r

if __name__ == '__main__':
    a,b=[ int(x.strip()) for x in input().strip().split() ]

    l1=set()
    for i in range(int(a),int(b)+1):
        if prime(i):
            l1.add(i)
    l1=list(l1)

    comb=set()
    for i in range(len(l1)):
        for j in range(len(l1)):
            if i!=j:
                comb.add(int(str(l1[i])+str(l1[j])))
    comb=list(comb)

    res=set()
    for n in comb:
        if prime(n):
            res.add(n)
    res=list(res)

    print(fibonacci(min(res),max(res),len(res)),sep='',end='')
