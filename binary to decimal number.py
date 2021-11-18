num=int(input('enter your binary number to convert in decimal'))
a=2
sum=0
i=0
while num>0:
    b=num%10 
    if b!=0:
        sum=sum+a**i
    i=i+1
    num=num//10
print(sum)
