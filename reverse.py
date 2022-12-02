def rev(n):
    s=0
    while n>=1:
        r=n%10
        n=n//10
        s=s*10+r
        
n=int(input('enter a no'))
res=rev(n)
print(res)
        
        
    
