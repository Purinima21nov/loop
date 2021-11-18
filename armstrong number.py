n=int(input('enter a value'))
a=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if a==sum:
    print("yes")
else:
    print("no")