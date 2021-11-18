n=int(input('enter'))
a=n
sum=0
while n>0:
    m=n%10
    n=n//10
    sum=sum+m
if a%sum==0:
    print('yes')
else:
    print('no')    
    