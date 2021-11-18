n=int(input('enter'))
a=1
b=1
while a<=n:
    if a==n:
        print(b,'/',a,"!")
    else:
        print(b,'/',a,'!',end="+") 
    a=a+1