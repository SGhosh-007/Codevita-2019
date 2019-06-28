for _ in range(int(input())):
    k=int(input())
    l=list(map(int,input().split()))
    m=l[:]
    n=l[:]
    c=0
    while True:
        k=0
        for i in l:
            n[i-1]=m[k]
            k+=1
        m=n[:]
        print(m)
        c+=1
        if m==l:
            break
    print(c)
