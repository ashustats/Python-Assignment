a=[lambda x=x:x*10 for x in range(1,11)]
for val in a:
    print(val())
