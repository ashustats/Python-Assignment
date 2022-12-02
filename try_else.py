a=int(input('enter a no. - '))
b=int(input('enter a no. - '))
try:
    a,b=10/0
    c=a/b
except Exception:
    print('check your denominator')
    print(Exception)
else:
    print('hi i am else block')
