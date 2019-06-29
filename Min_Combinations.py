for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    k=min(a,b)
    if k!=0 and a%k==0 and b%k==0:
        print(k)
    else:
        for i in range(1,k//2+1):
            if a%i==0 and b%i==0:
                res=i
        print(res)
