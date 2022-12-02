def foo(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        return foo(m-2)+foo(m-1)
print(foo(8))
