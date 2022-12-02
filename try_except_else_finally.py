try:
    f=open('a to z.txt','r')
except IOError:
    print('file not found')
else:
    print('ok bye')
finally:
    print('thank to visit')
