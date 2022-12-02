def p(n):
    if n<0:
        return
    print(str(n),end=' ')
    p(n-1)
p(5)
