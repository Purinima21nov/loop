n=int(input('enter'))
a=n
sum=0
while a>0:
    f=1
    i=1
    r=a%10
    while i<=r:
        f=f*i
        i=i+1
    sum=sum+f
    a=a//10
if sum==n:
    print("yes")    
else:
    print("no")