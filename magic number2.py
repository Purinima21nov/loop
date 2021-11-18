num=int(input("enter a value:"))
num1=num
sum=0
while num1!=0:
     rem=num1%10
     sum=sum+rem
     num1=num1//10
rev=0
num2=sum
while num2!=0:
    rem2=num2%10
    rev=rev*10+rem2
    num2=num2//10
if sum*rev==num:
    print('yes ')
else:
    print('no')