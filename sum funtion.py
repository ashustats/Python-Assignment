def sum(n,m):
    if m==0:
        return n
    else:
        c=1+sum(n,m-1)
        return c
res=sum(4,1)
print(res)
