def prime(n):
    c=0
    i=1
    while n>=i:
        r=n%i
        if r==0:
            c+=1
        i+=1
    if c==2:
        print('prime no')
    else:
        print('not a prime')
n=int(input('enter a no- '))
prime(n)
prime(n)    
prime(n)
