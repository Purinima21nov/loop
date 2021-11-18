num=int(input("enter a value:"))
a=num
sum=0
while num!=0:
    m=num%10
    num=num//10
    sum=sum+m
rev=sum
sum2=0
while rev!=0:
    m2=rev%10
    rev=rev//10
    sum2=sum2*10+m
if sum2*sum==a:
    print('yes')
else:
    print('no')