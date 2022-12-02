def fun(n):
    if n==0:
        return 1
    else:
        c=n*fun(n-1)
        return c
num=4
res=fun(num)
print(res)
