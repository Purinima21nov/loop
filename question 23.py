num1=int(input('enter the starting value'))
num2=int(input('enter the ending value'))
sum1=0
sum2=0
while num1<=num2:
    if num1%2==0:
        sum1=sum1+num1
    else:
        sum2=sum2+num1
    num1=num1+1
print("sum of even number",sum1)
print("sum of odd number",sum2)

        